"""
Sign Language MCP API - Flask Application
Educational project demonstrating API concepts and MCP (Model Context Protocol) integration

This Flask API demonstrates key concepts:
1. Discovery Endpoints - How clients can discover available resources (like MCP tool discovery)
2. Data Endpoints - How to retrieve specific data
3. Self-describing API - The /capabilities endpoint mirrors MCP's schema description

Perfect for teaching students about REST APIs and how they relate to AI tool integration!
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import database

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (important for web-based AI tools)

# API version for versioning support
API_VERSION = "1.0.0"
API_NAME = "Sign Language MCP API"


# ============================================================================
# ROOT & HEALTH ENDPOINTS
# ============================================================================

@app.route('/')
def root():
    """
    Root endpoint - provides a welcome message and quick start guide.
    This is the first place users land when they visit the API.
    
    TEACHING POINT: Always provide helpful guidance at the root!
    """
    return jsonify({
        "message": "Welcome to the Sign Language MCP API!",
        "description": "Educational API for learning sign language across Auslan, JSL, and International Sign",
        "version": API_VERSION,
        "quick_start": {
            "1_discover_words": "/api/v1/words",
            "2_discover_languages": "/api/v1/languages",
            "3_get_sign": "/api/v1/signs/{word}",
            "4_get_specific": "/api/v1/signs/{word}/{language}",
            "5_see_all_capabilities": "/api/v1/capabilities"
        },
        "teaching_note": "This API demonstrates how discovery endpoints work, similar to MCP tool discovery in AI systems!"
    })


@app.route('/api/v1/health')
def health():
    """
    Health check endpoint - used to verify the API is running.
    
    TEACHING POINT: Health checks are essential for monitoring and deployment!
    """
    return jsonify({
        "status": "healthy",
        "api_name": API_NAME,
        "version": API_VERSION
    })


# ============================================================================
# DISCOVERY ENDPOINTS (MCP Teaching Points!)
# ============================================================================

@app.route('/api/v1/words')
def list_words():
    """
    Discovery endpoint: List all available words.
    
    MCP TEACHING POINT: This is like MCP's tool discovery!
    - Before using an MCP tool, the AI discovers what tools are available
    - Before querying a sign, the user discovers what words are available
    - This pattern of "discover then use" is fundamental to both APIs and MCP
    """
    words = database.get_all_words()
    return jsonify({
        "words": words,
        "count": len(words),
        "hint": "Use GET /api/v1/signs/{word} to get sign descriptions"
    })


@app.route('/api/v1/languages')
def list_languages():
    """
    Discovery endpoint: List all supported sign languages.
    
    MCP TEACHING POINT: Just like discovering tools, we discover available resources!
    - This tells users what languages they can query
    - Similar to how MCP describes parameter options for tools
    """
    languages = database.get_all_languages()
    return jsonify({
        "languages": [
            {"code": code, "name": name}
            for code, name in languages.items()
        ],
        "count": len(languages),
        "hint": "Use language codes in GET /api/v1/signs/{word}/{language}"
    })


@app.route('/api/v1/capabilities')
def capabilities():
    """
    META endpoint: Describes ALL API capabilities in one place!
    
    MCP TEACHING POINT: This is the most important teaching endpoint!
    - In MCP, the server describes its tools/resources/prompts in a schema
    - This endpoint does the same thing for our REST API
    - It's "self-documenting" - the API describes itself!
    - An AI agent could read this endpoint to understand how to use the entire API
    
    This demonstrates the key concept: APIs can be self-describing, 
    making them easier for both humans and AI to understand and use.
    """
    return jsonify({
        "api_name": API_NAME,
        "version": API_VERSION,
        "description": "Educational API for querying sign language descriptions across multiple sign languages",
        "mcp_teaching_note": "This endpoint demonstrates how APIs can be self-describing, similar to MCP's schema. An AI could read this to understand how to use the API!",
        "endpoints": {
            "discovery": [
                {
                    "path": "/api/v1/words",
                    "method": "GET",
                    "description": "List all available words that have sign language descriptions",
                    "parameters": [],
                    "example": "/api/v1/words"
                },
                {
                    "path": "/api/v1/languages",
                    "method": "GET",
                    "description": "List all supported sign languages",
                    "parameters": [],
                    "example": "/api/v1/languages"
                },
                {
                    "path": "/api/v1/capabilities",
                    "method": "GET",
                    "description": "Get API capabilities (this endpoint!) - the META endpoint",
                    "parameters": [],
                    "example": "/api/v1/capabilities"
                }
            ],
            "data": [
                {
                    "path": "/api/v1/signs/<word>",
                    "method": "GET",
                    "description": "Get sign descriptions for a word in ALL languages",
                    "parameters": [
                        {
                            "name": "word",
                            "type": "path",
                            "required": True,
                            "description": "The word to look up",
                            "available_values": database.get_all_words()
                        }
                    ],
                    "example": "/api/v1/signs/hello"
                },
                {
                    "path": "/api/v1/signs/<word>/<language>",
                    "method": "GET",
                    "description": "Get sign description for a word in a SPECIFIC language",
                    "parameters": [
                        {
                            "name": "word",
                            "type": "path",
                            "required": True,
                            "description": "The word to look up",
                            "available_values": database.get_all_words()
                        },
                        {
                            "name": "language",
                            "type": "path",
                            "required": True,
                            "description": "The sign language code",
                            "available_values": list(database.get_all_languages().keys())
                        }
                    ],
                    "example": "/api/v1/signs/hello/auslan"
                }
            ],
            "utility": [
                {
                    "path": "/api/v1/health",
                    "method": "GET",
                    "description": "Health check endpoint",
                    "parameters": [],
                    "example": "/api/v1/health"
                },
                {
                    "path": "/",
                    "method": "GET",
                    "description": "Root endpoint with quick start guide",
                    "parameters": [],
                    "example": "/"
                }
            ]
        }
    })


# ============================================================================
# DATA ENDPOINTS
# ============================================================================

@app.route('/api/v1/signs/<word>')
def get_sign_all_languages(word):
    """
    Get sign descriptions for a word in ALL languages.
    
    TEACHING POINT: Error handling with helpful messages!
    - When something isn't found, tell the user what IS available
    - This makes the API educational and user-friendly
    """
    # Convert to lowercase for case-insensitive matching
    word = word.lower()
    
    sign_data = database.get_sign(word)
    
    if sign_data is None:
        # Return helpful error with available options
        return jsonify({
            "error": "Word not found",
            "word": word,
            "message": f"The word '{word}' is not in our database.",
            "available_words": database.get_all_words(),
            "hint": "Try one of the available words listed above"
        }), 404
    
    return jsonify({
        "word": word,
        "languages": sign_data,
        "count": len(sign_data)
    })


@app.route('/api/v1/signs/<word>/<language>')
def get_sign_specific_language(word, language):
    """
    Get sign description for a word in a SPECIFIC language.
    
    TEACHING POINT: Detailed error handling!
    - Check if word exists
    - Check if language exists
    - Provide helpful error messages for each case
    """
    # Convert to lowercase for case-insensitive matching
    word = word.lower()
    language = language.lower()
    
    # First check if word exists
    if word not in database.get_all_words():
        return jsonify({
            "error": "Word not found",
            "word": word,
            "message": f"The word '{word}' is not in our database.",
            "available_words": database.get_all_words(),
            "hint": "Try one of the available words listed above"
        }), 404
    
    # Then check if language exists
    if language not in database.get_all_languages():
        return jsonify({
            "error": "Language not found",
            "language": language,
            "message": f"The language code '{language}' is not supported.",
            "available_languages": [
                {"code": code, "name": name}
                for code, name in database.get_all_languages().items()
            ],
            "hint": "Try one of the available language codes listed above"
        }), 404
    
    # Get the specific sign data
    sign_data = database.get_sign(word, language)
    
    return jsonify({
        "word": word,
        "language": language,
        "sign": sign_data[language]
    })


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print(f"🚀 Starting {API_NAME} v{API_VERSION}")
    print("=" * 60)
    print("\n📚 TEACHING POINTS:")
    print("   - Discovery Endpoints: How to find available resources")
    print("   - Self-Describing API: /capabilities shows everything")
    print("   - MCP Connection: Similar patterns to AI tool integration")
    print("\n🔗 USEFUL URLs:")
    print("   Root:         http://localhost:5000/")
    print("   Words:        http://localhost:5000/api/v1/words")
    print("   Languages:    http://localhost:5000/api/v1/languages")
    print("   Capabilities: http://localhost:5000/api/v1/capabilities")
    print("   Example:      http://localhost:5000/api/v1/signs/hello")
    print("\n" + "=" * 60)
    
    # Run the Flask app
    # SECURITY NOTE: debug=True is only for local development/education!
    # For production deployment, use debug=False and a production WSGI server like Gunicorn
    app.run(host='0.0.0.0', port=5000, debug=True)
