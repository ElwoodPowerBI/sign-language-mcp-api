# Sign Language MCP API 🤟

**Educational REST API for learning about Model Context Protocol (MCP) integration with AI systems**

This project is designed for students to learn about:
- REST API design and development
- How discovery endpoints work (similar to MCP tool discovery)
- Self-describing APIs that AI agents can understand
- The connection between traditional APIs and AI tool integration
- Sign language basics across multiple languages

Perfect for AI clubs, coding bootcamps, or anyone wanting to understand how APIs connect to Large Language Models (LLMs)!

---

## 🎯 What is This Project?

This is a **Flask-based REST API** that provides sign language descriptions for common words across three sign languages:
- **Auslan** (Australian Sign Language)
- **JSL** (Japanese Sign Language)  
- **IS** (International Sign)

The API demonstrates key concepts that mirror how **Model Context Protocol (MCP)** works:
1. **Discovery** - Finding what resources/tools are available
2. **Self-description** - APIs that describe themselves
3. **Structured data** - How AI agents understand and use tools

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation & Running

```bash
# 1. Clone the repository
git clone https://github.com/YOUR-USERNAME/sign-language-mcp-api.git
cd sign-language-mcp-api

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the API
python app.py
```

The API will start on `http://localhost:5000`

### First API Calls

Try these URLs in your browser:
```
http://localhost:5000/                          # Welcome page
http://localhost:5000/api/v1/words              # See all available words
http://localhost:5000/api/v1/languages          # See supported languages
http://localhost:5000/api/v1/capabilities       # See ALL API capabilities
http://localhost:5000/api/v1/signs/hello        # Get "hello" in all languages
http://localhost:5000/api/v1/signs/hello/auslan # Get "hello" in Auslan only
```

---

## 📚 API Endpoints Documentation

### Discovery Endpoints (MCP Teaching Points!)

#### `GET /api/v1/words`
**Discover what words are available**

Response:
```json
{
  "words": ["hello", "help", "please", "sorry", "thank_you"],
  "count": 5,
  "hint": "Use GET /api/v1/signs/{word} to get sign descriptions"
}
```

**Teaching Point:** This is like MCP tool discovery - before using a tool, discover what's available!

---

#### `GET /api/v1/languages`
**Discover what sign languages are supported**

Response:
```json
{
  "languages": [
    {"code": "auslan", "name": "Australian Sign Language"},
    {"code": "jsl", "name": "Japanese Sign Language"},
    {"code": "is", "name": "International Sign"}
  ],
  "count": 3,
  "hint": "Use language codes in GET /api/v1/signs/{word}/{language}"
}
```

**Teaching Point:** Similar to MCP describing parameter options for tools!

---

#### `GET /api/v1/capabilities`
**META endpoint - The API describes itself!**

This is the **most important endpoint** for understanding MCP concepts!

Response includes:
- Complete API description
- All available endpoints
- Parameters for each endpoint
- Example usage
- Available values for parameters

**Teaching Point:** In MCP, servers describe their capabilities using a schema. This endpoint does the same for our REST API! An AI agent could read this endpoint and understand how to use the entire API.

---

### Data Endpoints

#### `GET /api/v1/signs/<word>`
**Get sign descriptions for a word in ALL languages**

Example: `GET /api/v1/signs/hello`

Response:
```json
{
  "word": "hello",
  "languages": {
    "auslan": {
      "language_full": "Australian Sign Language",
      "description": "Open hand, palm facing outward...",
      "handshape": "Open hand with fingers together",
      "movement": "Small arc outward from forehead",
      "facial_expression": "Friendly smile"
    },
    "jsl": { ... },
    "is": { ... }
  },
  "count": 3
}
```

---

#### `GET /api/v1/signs/<word>/<language>`
**Get sign for a specific word in a specific language**

Example: `GET /api/v1/signs/thank_you/auslan`

Response:
```json
{
  "word": "thank_you",
  "language": "auslan",
  "sign": {
    "language_full": "Australian Sign Language",
    "description": "Flat hand starts at chin, palm facing body...",
    "handshape": "Flat hand, fingers together",
    "movement": "Forward and downward from chin",
    "facial_expression": "Grateful smile"
  }
}
```

---

### Utility Endpoints

#### `GET /api/v1/health`
**Health check - verify the API is running**

Response:
```json
{
  "status": "healthy",
  "api_name": "Sign Language MCP API",
  "version": "1.0.0"
}
```

---

#### `GET /`
**Root endpoint with welcome message and quick start guide**

---

## 🎓 MCP Teaching Section

### What is MCP (Model Context Protocol)?

MCP is a protocol that allows AI models (like ChatGPT, Claude) to use **tools** and access **resources**. Think of it as a standardized way for AI to:
1. **Discover** what tools are available
2. **Understand** how to use each tool
3. **Execute** tools to get information or perform actions

### How This API Demonstrates MCP Concepts

| MCP Concept | API Equivalent | Why It Matters |
|-------------|----------------|----------------|
| **Tool Discovery** | `GET /api/v1/words` | AI needs to know what tools exist before using them |
| **Schema Description** | `GET /api/v1/capabilities` | Both APIs and MCP servers describe themselves so clients/AI know how to use them |
| **Tool Parameters** | `word` and `language` parameters | Tools need inputs - schemas define what's required and optional |
| **Tool Execution** | `GET /api/v1/signs/{word}` | Actually using the tool/API to get data |
| **Error Handling** | 404 responses with available options | Good tools guide users when something goes wrong |

### The Key Insight

**REST APIs and MCP tools are conceptually similar:**
- Both need discovery mechanisms
- Both need clear descriptions of capabilities
- Both need to handle inputs and return structured outputs
- Both benefit from being self-documenting

This API helps students understand traditional REST before learning MCP, making MCP concepts easier to grasp!

---

## 🎯 Learning Path for AI Club (3-Week Curriculum)

### Week 1: Understanding REST APIs
**Goal:** Learn how APIs work using this project

Activities:
1. Clone and run the API locally
2. Test all endpoints using browser and `curl`
3. Understand JSON responses
4. Read the code in `app.py` - follow the comments
5. Modify database to add a new word

**Exercise:** Add "goodbye" sign to all three languages in `database.py`

---

### Week 2: Discovery and Self-Description
**Goal:** Understand how APIs can be self-describing

Activities:
1. Study the `/api/v1/capabilities` endpoint
2. Compare it to the MCP schema in `mcp/sign_language_mcp.json`
3. Understand why discovery endpoints matter
4. Create a simple Python script that calls the API

**Exercise:** Write a Python script that:
- Calls `/api/v1/words` to discover available words
- For each word, calls `/api/v1/signs/{word}` to get descriptions
- Prints a formatted report

---

### Week 3: MCP Integration Concepts
**Goal:** Connect REST API knowledge to MCP

Activities:
1. Study the `mcp/sign_language_mcp.json` file
2. Compare MCP tool definitions to API endpoints
3. Discuss how an AI would use this API
4. Explore real MCP servers (if available)

**Exercise:** 
- Design an MCP tool wrapper for this API
- Write pseudo-code for how an AI agent would discover and use this API
- Discuss: "What would make an API easier for AI to use?"

---

## 🚢 Deployment Options

### Option 1: Replit (Easiest for Students)
1. Create a new Repl, import from GitHub
2. Replit auto-detects Python and installs requirements
3. Click "Run" - that's it!

### Option 2: Render (Free Tier)
1. Connect your GitHub repo to Render
2. Choose "Web Service"
3. Build command: `pip install -r requirements.txt`
4. Start command: `python app.py`

### Option 3: Railway (Modern & Easy)
1. Connect GitHub repo
2. Railway auto-detects Python
3. Deploys automatically on push

### Option 4: PythonAnywhere (Educational Friendly)
1. Upload files to PythonAnywhere
2. Set up a web app using Flask
3. Configure WSGI file to point to `app.py`

---

## 🔧 How to Extend This Project

### Add More Words
Edit `database.py` and add entries to `SIGN_DATABASE`:
```python
"goodbye": {
    "auslan": { ... },
    "jsl": { ... },
    "is": { ... }
}
```

### Add More Languages
1. Add language to `SUPPORTED_LANGUAGES` in `database.py`
2. Add sign descriptions for that language to each word
3. Update MCP schema enum in `mcp/sign_language_mcp.json`

### Add More Features
Ideas for student projects:
- Add images/videos for signs
- Add difficulty ratings
- Add categories (greetings, emotions, questions)
- Add user favorites system
- Add quiz/practice mode endpoint
- Add search functionality
- Add pronunciation guides

### Connect to a Real Database
Replace the in-memory dictionary with:
- SQLite (simplest)
- PostgreSQL (production-ready)
- MongoDB (if you want NoSQL experience)

---

## 📖 Sign Language Resources

Want to learn more about sign languages?
- [Auslan Signbank](https://auslan.org.au/) - Australian Sign Language
- [Japanese Sign Language Dictionary](https://www.jfd.or.jp/) - JSL Resources
- [World Federation of the Deaf](https://wfdeaf.org/) - International Sign info
- [Sign Language 101](https://www.signlanguage101.com/) - Learning resources

---

## 🤝 Contributing

This is an educational project! Contributions welcome:
- Add more words and signs
- Improve documentation
- Add more teaching examples
- Fix bugs
- Add tests

---

## 📝 License

MIT License - Free to use for educational purposes!

---

## 🙏 Acknowledgments

Created for AI Club educational purposes. Special thanks to:
- Sign language communities worldwide
- Open source contributors
- Students learning about APIs and AI integration

---

## 💡 Questions or Issues?

Open an issue on GitHub or ask in your AI Club sessions!

**Happy Learning! 🎉🤟**