import json
import os
import subprocess

from google.adk.agents import Agent


def init_astro_project(project_name: str) -> dict:
    """Initialize a new Astro project with React support."""
    try:
        # Ensure npm is available
        command = f"npm create astro@latest {project_name} -- --template minimal --yes"
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=".",
        )
        if result.returncode == 0:
            return {
                "status": "success",
                "output": result.stdout,
                "project_dir": os.path.join(os.getcwd(), project_name),
            }
        else:
            return {"status": "error", "error": result.stderr}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def add_react_integration(project_dir: str) -> dict:
    """Add React integration to the Astro project."""
    try:
        if not os.path.exists(project_dir):
            return {"status": "error", "error": "Project directory does not exist."}
        
        # Add Astro React integration
        result = subprocess.run(
            ["npx", "astro", "add", "react", "--yes"],
            capture_output=True,
            text=True,
            cwd=project_dir
        )
        
        if result.returncode == 0:
            return {
                "status": "success",
                "output": result.stdout,
                "message": "React integration added successfully"
            }
        else:
            return {"status": "error", "error": result.stderr}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def add_tailwind_integration(project_dir: str) -> dict:
    """Add Tailwind CSS integration to the Astro project."""
    try:
        if not os.path.exists(project_dir):
            return {"status": "error", "error": "Project directory does not exist."}
        
        # Add Astro Tailwind integration
        result = subprocess.run(
            ["npx", "astro", "add", "tailwind", "--yes"],
            capture_output=True,
            text=True,
            cwd=project_dir
        )
        
        if result.returncode == 0:
            return {
                "status": "success",
                "output": result.stdout,
                "message": "Tailwind CSS integration added successfully"
            }
        else:
            return {"status": "error", "error": result.stderr}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def write_astro_page(project_dir: str, page_name: str, content: str) -> dict:
    """Write an Astro page file with actual code content."""
    try:
        if not os.path.exists(project_dir):
            return {"status": "error", "error": "Project directory does not exist."}
        
        pages_dir = os.path.join(project_dir, "src", "pages")
        os.makedirs(pages_dir, exist_ok=True)
        
        file_path = os.path.join(pages_dir, f"{page_name}.astro")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        return {
            "status": "success",
            "message": f"Created page: {page_name}.astro",
            "file_path": file_path
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def write_react_component(project_dir: str, component_name: str, content: str) -> dict:
    """Write a React component file (.jsx or .tsx)."""
    try:
        if not os.path.exists(project_dir):
            return {"status": "error", "error": "Project directory does not exist."}
        
        components_dir = os.path.join(project_dir, "src", "components")
        os.makedirs(components_dir, exist_ok=True)
        
        # Use .jsx extension for React components
        file_path = os.path.join(components_dir, f"{component_name}.jsx")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        return {
            "status": "success",
            "message": f"Created React component: {component_name}.jsx",
            "file_path": file_path
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def write_astro_component(project_dir: str, component_name: str, content: str) -> dict:
    """Write an Astro component file with actual code content."""
    try:
        if not os.path.exists(project_dir):
            return {"status": "error", "error": "Project directory does not exist."}
        
        components_dir = os.path.join(project_dir, "src", "components")
        os.makedirs(components_dir, exist_ok=True)
        
        file_path = os.path.join(components_dir, f"{component_name}.astro")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        return {
            "status": "success",
            "message": f"Created component: {component_name}.astro",
            "file_path": file_path
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def write_css_file(project_dir: str, filename: str, content: str) -> dict:
    """Write a CSS file for styling."""
    try:
        if not os.path.exists(project_dir):
            return {"status": "error", "error": "Project directory does not exist."}
        
        styles_dir = os.path.join(project_dir, "src", "styles")
        os.makedirs(styles_dir, exist_ok=True)
        
        file_path = os.path.join(styles_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        return {
            "status": "success",
            "message": f"Created CSS file: {filename}",
            "file_path": file_path
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def write_layout_file(project_dir: str, layout_name: str, content: str) -> dict:
    """Write an Astro layout file."""
    try:
        if not os.path.exists(project_dir):
            return {"status": "error", "error": "Project directory does not exist."}
        
        layouts_dir = os.path.join(project_dir, "src", "layouts")
        os.makedirs(layouts_dir, exist_ok=True)
        
        file_path = os.path.join(layouts_dir, f"{layout_name}.astro")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        return {
            "status": "success",
            "message": f"Created layout: {layout_name}.astro",
            "file_path": file_path
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def install_dependencies(project_dir: str) -> dict:
    """Install npm dependencies for the Astro project."""
    try:
        if not os.path.exists(project_dir):
            return {"status": "error", "error": "Project directory does not exist."}
        
        result = subprocess.run(
            ["npm", "install"],
            capture_output=True,
            text=True,
            cwd=project_dir
        )
        
        if result.returncode == 0:
            return {
                "status": "success",
                "output": result.stdout,
                "message": "Dependencies installed successfully"
            }
        else:
            return {"status": "error", "error": result.stderr}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def build_astro_project(project_dir: str) -> dict:
    """Build the Astro project."""
    try:
        if not os.path.exists(project_dir):
            return {"status": "error", "error": "Project directory does not exist."}
        result = subprocess.run(
            ["npm", "run", "build"], capture_output=True, text=True, cwd=project_dir
        )
        if result.returncode == 0:
            return {
                "status": "success",
                "output": result.stdout,
                "build_dir": os.path.join(project_dir, "dist"),
            }
        else:
            return {"status": "error", "error": result.stderr}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def get_design_data() -> dict:
    """Retrieve design data from the JSON file saved by mike."""
    try:
        with open("design_data.json", "r") as f:
            data = json.load(f)
        return {"data": data}
    except FileNotFoundError:
        return {
            "error": "Design data not found. Please ensure mike has saved the data."
        }
    except Exception as e:
        return {"error": str(e)}


def get_requirements_data() -> dict:
    """Retrieve requirements data from the JSON file saved by arch."""
    try:
        with open("requirements_data.json", "r") as f:
            data = json.load(f)
        return {"data": data}
    except FileNotFoundError:
        return {
            "error": "Requirements data not found. Please ensure arch has saved the data."
        }
    except Exception as e:
        return {"error": str(e)}


def get_ui_plan() -> dict:
    """Retrieve UI component plan from the JSON file saved by ui_designer."""
    try:
        with open("ui_plan.json", "r") as f:
            data = json.load(f)
        return {"data": data}
    except FileNotFoundError:
        return {
            "error": "UI plan not found. Please ensure ui_designer has saved the plan."
        }
    except Exception as e:
        return {"error": str(e)}


bob_agent = Agent(
    name="bob",
    model="gemini-2.0-flash",
    description="Agent responsible for building the website using Astro with React integration by writing actual code files.",
    instruction="""You are the builder agent Bob. When called, introduce yourself first.

Your job is to ACTUALLY CODE AND BUILD the website with Astro and React, not just provide templates.

Follow these steps:
1. Get the requirements data from arch using get_requirements_data
2. Get the design data from mike using get_design_data
3. Get the UI component plan from ui_designer using get_ui_plan
4. Initialize an Astro project using init_astro_project with a meaningful project name
5. Add React integration using add_react_integration
6. Add Tailwind CSS integration using add_tailwind_integration
7. WRITE ACTUAL CODE FILES:
   - Create a Layout file with proper HTML structure, meta tags, and design styling
   - Create React components (.jsx) for interactive UI elements using write_react_component
   - Create Astro components (.astro) for static sections using write_astro_component
   - Create Page files (.astro) that import and use the components
   - Create CSS files if needed (Tailwind will handle most styling)
8. Implement the UI plan provided by ui_designer with the suggested components
9. Install dependencies using install_dependencies
10. Build the project using build_astro_project

IMPORTANT: You must write the FULL code content for each file, not templates or placeholders.

React Components (.jsx):
- Use functional components with hooks
- Apply Tailwind CSS classes for styling
- Make them interactive with state when needed
- Export default or named exports
- Example: Button, Navbar, Card components

Astro Pages (.astro):
- Import React components with client:load or client:visible directives
- Use layouts for consistent structure
- Include proper meta tags and SEO
- Example: <Button client:load>Click me</Button>

Styling:
- Use Tailwind CSS utility classes
- Match colors, fonts from design data
- Implement responsive design (mobile-first)
- Add hover effects and transitions

After building successfully, tell the user the build is complete and ready for packaging.""",
    tools=[
        init_astro_project,
        add_react_integration,
        add_tailwind_integration,
        write_astro_page,
        write_react_component,
        write_astro_component,
        write_css_file,
        write_layout_file,
        install_dependencies,
        build_astro_project,
        get_design_data,
        get_requirements_data,
        get_ui_plan,
    ],
)
