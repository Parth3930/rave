import json
import os

from google.adk.agents import Agent


def search_component_library(component_type: str, library: str = "shadcn") -> dict:
    """Search for UI components from popular React component libraries."""
    # Component suggestions from popular libraries
    component_suggestions = {
        "shadcn": {
            "button": {
                "code": """import { Button } from "@/components/ui/button"

export default function ButtonDemo() {
  return <Button>Click me</Button>
}""",
                "description": "A customizable button component with variants",
                "install": "npx shadcn-ui@latest add button"
            },
            "card": {
                "code": """import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"

export default function CardDemo() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Card Title</CardTitle>
        <CardDescription>Card Description</CardDescription>
      </CardHeader>
      <CardContent>
        <p>Card Content</p>
      </CardContent>
    </Card>
  )
}""",
                "description": "A flexible card component for content containers",
                "install": "npx shadcn-ui@latest add card"
            },
            "navbar": {
                "code": """import { navigationMenuTriggerStyle } from "@/components/ui/navigation-menu"
import Link from "next/link"

export default function Navbar() {
  return (
    <nav className="flex items-center justify-between p-6">
      <div className="flex items-center space-x-8">
        <Link href="/" className={navigationMenuTriggerStyle()}>Home</Link>
        <Link href="/about" className={navigationMenuTriggerStyle()}>About</Link>
        <Link href="/contact" className={navigationMenuTriggerStyle()}>Contact</Link>
      </div>
    </nav>
  )
}""",
                "description": "A navigation menu component",
                "install": "npx shadcn-ui@latest add navigation-menu"
            },
            "hero": {
                "code": """export default function Hero() {
  return (
    <div className="relative overflow-hidden bg-gradient-to-b from-blue-50 to-white">
      <div className="mx-auto max-w-7xl px-6 py-24 sm:py-32 lg:px-8">
        <div className="text-center">
          <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">
            Welcome to Our Website
          </h1>
          <p className="mt-6 text-lg leading-8 text-gray-600">
            Build amazing experiences with modern design
          </p>
          <div className="mt-10 flex items-center justify-center gap-x-6">
            <Button>Get Started</Button>
            <Button variant="outline">Learn More</Button>
          </div>
        </div>
      </div>
    </div>
  )
}""",
                "description": "A hero section component",
                "install": "Built with Tailwind CSS"
            }
        },
        "react-bits": {
            "button": {
                "code": """export default function Button({ children, variant = "primary" }) {
  const variants = {
    primary: "bg-blue-600 hover:bg-blue-700 text-white",
    secondary: "bg-gray-200 hover:bg-gray-300 text-gray-900",
    outline: "border-2 border-blue-600 text-blue-600 hover:bg-blue-50"
  }
  
  return (
    <button className={`px-6 py-2 rounded-lg font-medium transition-all ${variants[variant]}`}>
      {children}
    </button>
  )
}""",
                "description": "A simple, customizable button component",
                "install": "Copy and paste into your components"
            }
        }
    }
    
    lib_components = component_suggestions.get(library, {})
    component = lib_components.get(component_type.lower())
    
    if component:
        return {
            "status": "success",
            "library": library,
            "component_type": component_type,
            "code": component["code"],
            "description": component["description"],
            "install": component["install"]
        }
    else:
        return {
            "status": "not_found",
            "message": f"Component '{component_type}' not found in {library}. Try: button, card, navbar, hero"
        }


def suggest_ui_components(page_type: str) -> dict:
    """Suggest appropriate UI components for different page types."""
    suggestions = {
        "landing": {
            "components": ["hero", "features", "cta", "testimonials", "footer"],
            "description": "Landing page with hero section, feature highlights, and call-to-action"
        },
        "portfolio": {
            "components": ["header", "hero", "project-grid", "about-section", "contact-form", "footer"],
            "description": "Portfolio site with project showcase and about section"
        },
        "blog": {
            "components": ["navbar", "hero", "blog-grid", "sidebar", "footer"],
            "description": "Blog layout with post listings and sidebar"
        },
        "business": {
            "components": ["navbar", "hero", "services", "about", "team", "contact", "footer"],
            "description": "Business website with services and team sections"
        },
        "ecommerce": {
            "components": ["navbar", "hero", "product-grid", "categories", "cart", "footer"],
            "description": "E-commerce site with product listings"
        }
    }
    
    suggestion = suggestions.get(page_type.lower(), {
        "components": ["navbar", "hero", "content", "footer"],
        "description": "Standard page layout"
    })
    
    return {
        "status": "success",
        "page_type": page_type,
        "suggested_components": suggestion["components"],
        "description": suggestion["description"]
    }


def create_component_structure(components_list: list) -> dict:
    """Create a component structure with recommendations for each component."""
    structure = {}
    
    for component in components_list:
        if component.lower() == "navbar":
            structure["Navbar"] = {
                "type": "component",
                "props": ["logo", "links"],
                "styling": "sticky top-0, backdrop-blur, shadow",
                "libraries": ["shadcn navigation-menu", "headless-ui"]
            }
        elif component.lower() == "hero":
            structure["Hero"] = {
                "type": "component",
                "props": ["title", "subtitle", "cta_buttons"],
                "styling": "gradient background, large typography, centered",
                "libraries": ["custom with Tailwind"]
            }
        elif component.lower() == "card":
            structure["Card"] = {
                "type": "component",
                "props": ["title", "description", "image", "link"],
                "styling": "rounded, shadow, hover effects",
                "libraries": ["shadcn card", "react-bootstrap"]
            }
        elif component.lower() == "footer":
            structure["Footer"] = {
                "type": "component",
                "props": ["links", "social_media", "copyright"],
                "styling": "dark background, grid layout",
                "libraries": ["custom"]
            }
        elif component.lower() in ["button", "cta"]:
            structure["Button"] = {
                "type": "component",
                "props": ["text", "variant", "onClick"],
                "styling": "rounded, gradient, hover effects",
                "libraries": ["shadcn button", "react-bits"]
            }
        else:
            structure[component.title()] = {
                "type": "component",
                "props": ["content"],
                "styling": "responsive, modern",
                "libraries": ["custom"]
            }
    
    return {
        "status": "success",
        "component_structure": structure,
        "total_components": len(structure)
    }


def save_ui_plan(ui_data: dict) -> dict:
    """Save the UI component plan to a JSON file."""
    try:
        with open("ui_plan.json", "w") as f:
            json.dump(ui_data, f, indent=2)
        return {
            "status": "success",
            "message": "UI plan saved to ui_plan.json"
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


ui_designer_agent = Agent(
    name="ui_designer",
    model="gemini-2.0-flash",
    description="UI/UX specialist that helps design component structure and suggests React components from libraries.",
    instruction="""You are the UI Designer agent, an expert in modern web design and React component libraries.

When called, introduce yourself first.

Your responsibilities:
1. Analyze the requirements and design data (read from JSON files automatically)
2. Suggest appropriate UI components for the website type using suggest_ui_components
3. Search for specific components from libraries (shadcn, react-bits) using search_component_library
4. Create a complete component structure using create_component_structure
5. Provide specific component code and styling recommendations
6. AUTOMATICALLY save the UI plan using save_ui_plan WITHOUT asking for confirmation

IMPORTANT Guidelines:
- Suggest modern, beautiful, and functional components
- Prefer popular libraries like shadcn/ui for consistent design
- Consider responsive design and accessibility
- Provide specific Tailwind CSS classes for styling
- Think about component reusability
- Match the design data (colors, fonts) from Mike

After creating and saving the UI plan, your task is COMPLETE. Signal that Bob can now proceed with implementation. DO NOT wait for user confirmation.""",
    tools=[
        search_component_library,
        suggest_ui_components,
        create_component_structure,
        save_ui_plan,
    ],
)
