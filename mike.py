import json

from google.adk.agents import Agent


def ask_colors() -> dict:
    """Ask about color preferences."""
    return {"question": "What color scheme do you prefer for your website?"}


def ask_layout() -> dict:
    """Ask about layout preferences."""
    return {
        "question": "What layout style do you want (e.g., grid, single-page, multi-page)?"
    }


def ask_fonts() -> dict:
    """Ask about font preferences."""
    return {"question": "What fonts or typography do you prefer?"}


def ask_images() -> dict:
    """Ask about image and media needs."""
    return {"question": "Do you have specific images, logos, or media requirements?"}


def save_design_data(data: dict) -> dict:
    """Save the gathered design data to a JSON file for other agents to access."""
    try:
        with open("design_data.json", "w") as f:
            json.dump(data, f)
        return {"status": "success", "message": "Design data saved to design_data.json"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


mike_agent = Agent(
    name="mike",
    model="gemini-2.0-flash",
    description=(
        "Design agent that handles design aspects, asking about colors, layout, fonts, and visuals."
    ),
    instruction=(
        "You are the design agent Mike. When called, introduce yourself first. Ask the user one detailed question at a time about the design of the website, such as colors, layout, fonts, images, and any visual preferences. Wait for the user's response before asking the next question. Gather all design-related information step by step. After gathering all the information, AUTOMATICALLY use the save_design_data tool to save it WITHOUT asking for user confirmation. Once saved, your task is COMPLETE and you should signal that the next agent can proceed."
    ),
    tools=[ask_colors, ask_layout, ask_fonts, ask_images, save_design_data],
)
