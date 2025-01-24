from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
# Configure CORS to allow requests from Figma
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Initialize OpenAI client
client = OpenAI()

# Language code to full name mapping
LANGUAGE_MAP = {
    'es': 'Spanish',
    'fr': 'French',
    'fr-ca': 'French (Canada)',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'nl': 'Dutch',
    'pl': 'Polish',
    'ru': 'Russian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'zh': 'Chinese'
}

@app.route('/test', methods=['GET'])
def test():
    """Simple test endpoint to verify server is running"""
    return jsonify({
        "status": "ok",
        "message": "Server is running"
    })

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        text = data.get('text', '')
        action = data.get('action', '')
        target_language = data.get('targetLanguage', '')

        if not text or not action:
            return jsonify({"error": "Missing required fields"}), 400

        # Load appropriate system prompt based on action
        try:
            if action == 'Translate':
                system_prompt = open('system_prompt_translate.txt').read()
                # Convert language code to full name and add to the text
                full_language_name = LANGUAGE_MAP.get(target_language, 'English')  # Default to English if code not found
                text = f"Translate this text to {full_language_name}: {text}"
            elif action == 'Enhance':
                system_prompt = open('system_prompt_enhance.txt').read()
            elif action == 'Shorten':
                system_prompt = open('system_prompt_shorten.txt').read()
            else:
                return jsonify({"error": "Invalid action"}), 400
        except FileNotFoundError as e:
            print(f"System prompt file not found: {str(e)}")
            return jsonify({"error": "Server configuration error"}), 500

        if os.getenv('MOCK_RESPONSE') == 'true':
            time.sleep(1)  # Simulate API delay
            return jsonify({
                "response": f"Mock {action} response for: {text}"
            })

        # Make the API call to OpenAI
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": text}
                ]
            )
            generated_text = response.choices[0].message.content
            return jsonify({"response": generated_text})

        except Exception as e:
            print(f"OpenAI API error: {str(e)}")
            return jsonify({"error": "Failed to generate response"}), 500

    except Exception as e:
        print(f"Error in generate endpoint: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # For testing without OpenAI API, set this environment variable
    # os.environ['MOCK_RESPONSE'] = 'true'
    
    app.run(debug=True, port=5000)