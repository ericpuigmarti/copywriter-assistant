from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
import logging
from config import Config
import re

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
config = Config.get_config()

# Configure CORS
CORS(app, resources={
    r"/*": {
        "origins": ["*"],
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Accept"]
    }
})

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

@app.route('/enhance', methods=['POST'])
def enhance():
    try:
        data = request.json
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful copywriting assistant."},
                {"role": "user", "content": f"Enhance this text:\n\n{text}"}
            ]
        )
        
        enhanced_text = response.choices[0].message.content.strip()
        return jsonify({'enhancedText': enhanced_text})

    except Exception as e:
        logger.error(f"Enhancement error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/shorten', methods=['POST'])
def shorten():
    try:
        data = request.json
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful copywriting assistant."},
                {"role": "user", "content": f"Create a shorter version of this text:\n\n{text}"}
            ]
        )
        
        shortened_text = response.choices[0].message.content.strip()
        return jsonify({'shortenedText': shortened_text})

    except Exception as e:
        logger.error(f"Shortening error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.json
        text = data.get('text', '')
        target_language = data.get('targetLanguage', '')
        
        if not text or not target_language:
            return jsonify({'error': 'Text and target language are required'}), 400

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful translation assistant."},
                {"role": "user", "content": f"Translate this text to {target_language}:\n\n{text}"}
            ]
        )
        
        translated_text = response.choices[0].message.content.strip()
        return jsonify({'translatedText': translated_text})

    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        return jsonify({'error': str(e)}), 500

# Add quality check endpoint
@app.route('/quality-check', methods=['POST'])
def quality_check():
    try:
        data = request.json
        text = data.get('text', '')
        brand_guidelines = data.get('brandGuidelines', '')

        # Basic text metrics
        char_count = len(text)
        word_count = len(text.split())
        sentences = len(re.split(r'[.!?]+', text))
        
        # Estimate reading and speaking times
        reading_time = round(word_count / 250 * 60)  # Average reading speed: 250 words/min
        speaking_time = round(word_count / 150 * 60)  # Average speaking speed: 150 words/min

        # Calculate average word length
        word_length = round(char_count / word_count, 1) if word_count > 0 else 0
        
        # Calculate average sentence length
        sentence_length = round(word_count / sentences, 1) if sentences > 0 else 0

        # Get quality score from OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": open('system_prompt_qualityCheck.txt').read()},
                {"role": "user", "content": text}
            ]
        )
        
        # Extract score from response with better error handling
        response_text = response.choices[0].message.content
        try:
            # Look for "Score: X/100" pattern
            score_match = re.search(r'Score:\s*(\d+)', response_text)
            if score_match:
                score = int(score_match.group(1))
            else:
                # Fallback to a default score if pattern not found
                score = 70
                logger.warning(f"Could not extract score from response: {response_text}")
        except Exception as e:
            logger.error(f"Error parsing score: {e}")
            score = 70  # Default score if parsing fails

        return jsonify({
            'score': score,
            'metrics': {
                'characters': char_count,
                'words': word_count,
                'sentences': sentences,
                'readingTime': reading_time,
                'speakingTime': speaking_time,
                'wordLength': word_length,
                'sentenceLength': sentence_length
            }
        })

    except Exception as e:
        logger.error(f"Quality check error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logger.info("Starting server...")
    logger.info(f"OpenAI API key present: {'Yes' if os.getenv('OPENAI_API_KEY') else 'No'}")
    app.run(debug=True, port=5000)