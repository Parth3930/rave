import json

from google.adk.agents import Agent


def ask_purpose() -> dict:
    """Ask about the purpose of the website."""
    return {"question": "What is the main purpose of your website?"}


def ask_audience() -> dict:
    """Ask about the target audience."""
    return {"question": "Who is the target audience for your website?"}


def ask_features() -> dict:
    """Ask about key features."""
    return {"question": "What key features should your website have?"}


def save_requirements_data(data: dict) -> dict:
    """Save the gathered requirements data to a JSON file for other agents to access."""
    try:
        with open("requirements_data.json", "w") as f:
            json.dump(data, f)
        return {"status": "success", "message": "Requirements data saved to requirements_data.json"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


arch_agent = Agent(
    name="arch",
    model="gemini-2.0-flash",
    description=(
        "Agent that gathers detailed requirements for the website by asking questions one by one."
    ),
    instruction=(
        "You are the architect agent. When called, introduce yourself first. Ask the user detailed questions one by one about the website they want to build, such as its purpose, target audience, key features, content needs, and any specific requirements. Gather all necessary information step by step. After gathering all the information, AUTOMATICALLY use the save_requirements_data tool to save it WITHOUT asking for user confirmation. Once saved, your task is COMPLETE and you should signal that the next agent can proceed."
    ),
    tools=[ask_purpose, ask_audience, ask_features, save_requirements_data],
)
