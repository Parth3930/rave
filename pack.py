import os
import shutil
import zipfile

from google.adk.agents import Agent


def organize_files(source_dir: str, dest_dir: str) -> dict:
    """Organize files by copying them to a destination directory."""
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for item in os.listdir(source_dir):
            s = os.path.join(source_dir, item)
            d = os.path.join(dest_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        return {
            "status": "success",
            "message": f"Files organized from {source_dir} to {dest_dir}",
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def zip_website(source_dir: str, output_name: str = "website") -> dict:
    """Pack the website directory into a zip file in the current directory."""
    try:
        if not os.path.exists(source_dir):
            return {"status": "error", "error": f"Source directory {source_dir} does not exist."}
        
        # Create zip in current directory with timestamp
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_filename = f"{output_name}_{timestamp}.zip"
        zip_path = os.path.join(os.getcwd(), zip_filename)
        
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_dir)
                    zipf.write(file_path, arcname)
        
        file_size = os.path.getsize(zip_path)
        return {
            "status": "success",
            "zip_file": zip_path,
            "filename": zip_filename,
            "size_bytes": file_size,
            "message": f"Website packed into {zip_filename} ({file_size} bytes)"
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def deliver_to_user(zip_path: str) -> dict:
    """Deliver the zip file to the user and mark task as complete."""
    try:
        if not os.path.exists(zip_path):
            return {"status": "error", "error": f"Zip file {zip_path} not found."}
        
        abs_path = os.path.abspath(zip_path)
        file_size = os.path.getsize(abs_path)
        
        return {
            "status": "complete",
            "delivery_status": "ready",
            "zip_file_path": abs_path,
            "file_size": file_size,
            "message": f"✅ WEBSITE COMPLETE! Your website is ready at: {abs_path}",
            "instructions": "You can download the zip file from the path above. Extract it and open index.html to view your website."
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


pack_agent = Agent(
    name="pack",
    model="gemini-2.0-flash",
    description="Agent that packs the built website into a zip file and delivers it to the user.",
    instruction="""You are the packager agent. When called, introduce yourself first.

Your job is to package and deliver the website to the user:

1. Find the built website directory (usually the 'dist' folder from the build)
2. Use zip_website to pack the dist folder into a zip file
3. Use deliver_to_user to mark the delivery as complete and provide the file path to the user

IMPORTANT: After calling deliver_to_user successfully, you MUST:
- Tell the user their website is COMPLETE and READY
- Provide the FULL file path where they can find the zip file
- Tell them they can extract it to view their website
- DO NOT continue asking questions or looping
- Your job is DONE once delivery is complete

The user should receive a clear message with the zip file location.""",
    tools=[organize_files, zip_website, deliver_to_user],
)
