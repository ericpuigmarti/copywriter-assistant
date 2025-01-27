from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
import logging
from config import Config

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
config = Config.get_config()

# Configure CORS
CORS(app)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Test endpoint
@app.route('/test', methods=['GET'])
def test():
    return jsonify({
        'status': 'ok',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'server_url': config.SERVER_URL,
        'debug_mode': config.DEBUG
    })

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Log the incoming request
        logger.debug("Received request")
        logger.debug(f"Headers: {request.headers}")
        logger.debug(f"Data: {request.get_data(as_text=True)}")

        data = request.json
        if not data:
            logger.error("No JSON data received")
            return jsonify({'error': 'No data provided'}), 400

        text = data.get('text', '')
        action = data.get('action', '')
        target_language = data.get('targetLanguage', '')
        brand_guidelines = data.get('brandGuidelines', '')

        logger.debug(f"Processing request - Action: {action}, Text: {text}, Language: {target_language}")

        # Verify we have a language for translation
        if action == 'Translate' and not target_language:
            logger.error("No target language provided for translation")
            return jsonify({'error': 'Target language is required for translation'}), 400

        # Verify API key
        if not os.getenv('OPENAI_API_KEY'):
            logger.error("OpenAI API key not found")
            return jsonify({'error': 'OpenAI API key not configured'}), 500

        # Create base system message
        system_message = "You are a helpful copywriting assistant."
        if brand_guidelines:
            system_message += f"\n\nBrand Guidelines:\n{brand_guidelines}"

        # Construct prompt based on action
        if action == 'Translate':
            prompt = f"Translate this text to {target_language} while maintaining the brand voice and style. The translation must be in {target_language}:\n\n{text}"
        elif action == 'Enhance':
            prompt = f"Enhance this text while maintaining the brand voice and style:\n\n{text}"
        elif action == 'Shorten':
            prompt = f"Create a shorter version of this text while maintaining the brand voice and style:\n\n{text}"
        else:
            logger.error(f"Invalid action: {action}")
            return jsonify({'error': 'Invalid action'}), 400

        logger.debug(f"Sending request to OpenAI with prompt: {prompt}")

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            logger.debug("Received response from OpenAI")
            logger.debug(f"OpenAI response: {response}")

            processed_text = response.choices[0].message.content.strip()
            logger.debug(f"Processed text: {processed_text}")
            
            return jsonify({'response': processed_text})

        except Exception as api_error:
            logger.error(f"OpenAI API Error: {str(api_error)}")
            return jsonify({'error': str(api_error)}), 500

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logger.info("Starting server...")
    logger.info(f"OpenAI API key present: {'Yes' if os.getenv('OPENAI_API_KEY') else 'No'}")
    app.run(debug=True, port=5000)