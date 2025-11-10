# RAVE - AI-Powered Multi-Agent Website Builder 🚀

RAVE (Rapid Astro Visual Engine) is an intelligent multi-agent system that collaboratively builds
complete, production-ready websites using Astro + React. Each specialized AI agent handles a
specific aspect of web development, from requirements gathering to deployment.

## 🎯 Overview

RAVE orchestrates a team of specialized AI agents to build websites automatically. The system
gathers requirements, designs the UI, writes actual code (not templates!), and delivers a complete,
deployable website.

## 🏗️ Architecture

### Agent Workflow

```
Root Agent (Manager)
    ↓
1. ARCH → Gathers Requirements
    ↓
2. MIKE → Designs Visual Elements
    ↓
3. UI_DESIGNER → Plans Component Structure
    ↓
4. BOB → Builds the Website (Astro + React)
    ↓
5. PACK → Packages & Delivers ZIP
```

## 🤖 Agent Roles

### 1. **ARCH** - Requirements Architect

- **Role**: Gathers detailed project requirements
- **Asks About**:
    - Website purpose and goals
    - Target audience
    - Key features and functionality
    - Content structure
- **Output**: `requirements_data.json`

### 2. **MIKE** - Design Specialist

- **Role**: Collects design preferences and visual requirements
- **Asks About**:
    - Color schemes and palettes
    - Layout preferences (grid, single-page, multi-page)
    - Typography and fonts
    - Images, logos, and media requirements
- **Output**: `design_data.json`

### 3. **UI_DESIGNER** - Component Architect

- **Role**: Plans UI component structure and selects React components
- **Capabilities**:
    - Suggests components based on website type (landing, portfolio, blog, etc.)
    - Searches component libraries (shadcn/ui, react-bits)
    - Creates detailed component structure
    - Provides Tailwind CSS styling recommendations
- **Output**: `ui_plan.json`

### 4. **BOB** - Builder & Developer

- **Role**: Actually codes and builds the website (NO TEMPLATES!)
- **Technology Stack**:
    - **Astro** - Modern static site generator
    - **React** - Interactive components
    - **Tailwind CSS** - Utility-first styling
- **Capabilities**:
    - Initializes Astro project with React integration
    - Writes actual code files:
        - React components (.jsx) for interactive elements
        - Astro pages (.astro) for static content
        - Layout files with proper HTML structure
        - CSS/Tailwind styling
    - Installs dependencies
    - Builds the production-ready website
- **Output**: Complete Astro project with `dist/` build folder

### 5. **PACK** - Packager & Deliverer

- **Role**: Packages and delivers the final website
- **Capabilities**:
    - Organizes project files
    - Creates timestamped ZIP archive
    - Provides download path to user
    - Signals completion (NO INFINITE LOOPS!)
- **Output**: `website_YYYYMMDD_HHMMSS.zip`

## 🚀 Features

✅ **Actual Code Generation** - Bob writes full, functional code (not templates!)
✅ **React Integration** - Modern, interactive components
✅ **Tailwind CSS** - Beautiful, responsive styling
✅ **Component Libraries** - Leverages shadcn/ui and react-bits
✅ **Production Ready** - Builds optimized static sites
✅ **Automated Workflow** - From requirements to deployment
✅ **No Infinite Loops** - Clear completion signals

## 📦 Installation

### Prerequisites

- Python 3.8+
- Node.js 18+ and npm
- Google ADK (Agent Development Kit)

### Setup

```bash
# Clone the repository
git clone https://github.com/Parth3930/rave.git
cd rave

# Install Python dependencies
pip install google-adk

# Set up environment variables
cp example.env .env
# Edit .env with your API keys
```

### Environment Variables

Create a `.env` file with:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

## 🎮 Usage

### Running RAVE

```python
from rave.agent import root_agent

# Start the website building process
response = root_agent.chat("I want to build a portfolio website")
```

### Workflow Example

1. **User**: "I want to build a portfolio website"
2. **ARCH**: Asks about purpose, audience, features
3. **MIKE**: Asks about colors, layout, fonts
4. **UI_DESIGNER**: Suggests components (navbar, hero, project-grid, footer)
5. **BOB**: Creates Astro + React project with actual code
6. **PACK**: Delivers `portfolio_20240115_143022.zip`

## 📁 Project Structure

```
rave/
├── __init__.py           # Package initialization
├── agent.py              # Root manager agent
├── arch.py               # Requirements architect
├── mike.py               # Design specialist
├── ui_designer.py        # UI/Component architect
├── bob.py                # Builder & developer
├── pack.py               # Packager & deliverer
├── README.md             # This file
├── .gitignore            # Git ignore rules
└── example.env           # Environment template
```

## 🔧 Technical Details

### Bob's Tools

- `init_astro_project()` - Initialize Astro project
- `add_react_integration()` - Add React support
- `add_tailwind_integration()` - Add Tailwind CSS
- `write_react_component()` - Create .jsx components
- `write_astro_component()` - Create .astro components
- `write_astro_page()` - Create pages
- `write_layout_file()` - Create layouts
- `write_css_file()` - Create stylesheets
- `install_dependencies()` - Install npm packages
- `build_astro_project()` - Build for production

### Output Structure

Generated websites follow this structure:

```
project_name/
├── src/
│   ├── components/       # React & Astro components
│   ├── layouts/          # Layout templates
│   ├── pages/            # Astro pages (routes)
│   └── styles/           # CSS files
├── dist/                 # Production build (zipped)
├── package.json          # Dependencies
├── astro.config.mjs      # Astro config
└── tailwind.config.cjs   # Tailwind config
```

## 🎨 Supported Website Types

- **Landing Pages** - Hero, features, CTA, testimonials
- **Portfolio Sites** - Project showcase, about, contact
- **Business Websites** - Services, team, contact forms
- **Blogs** - Post listings, sidebar, categories
- **E-commerce** - Product grids, categories

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License.

## 🔮 Future Enhancements

- [ ] Support for more frameworks (Next.js, SvelteKit)
- [ ] Database integration options
- [ ] CMS integration
- [ ] Deployment automation (Vercel, Netlify)
- [ ] A/B testing capabilities
- [ ] SEO optimization agent
- [ ] Analytics integration

## 👥 Team

Built with ❤️ by the Rover

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Note**: RAVE uses Google's Gemini 2.0 Flash model for all agents. Make sure you have a valid API
key.
