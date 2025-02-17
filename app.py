from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
import logging
from config import Config
import re
import json
from pathlib import Path
import random
import time

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
        "origins": ["https://www.figma.com"],
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Accept"],
        "expose_headers": ["Access-Control-Allow-Origin"],
        "supports_credentials": False,
        "send_wildcard": False
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
    start_time = time.time()
    try:
        data = request.json
        text = data.get('text', '')
        target_language = data.get('targetLanguage', '')
        
        if not text or not target_language:
            return jsonify({'error': 'Text and target language are required'}), 400

        # Log API call start
        api_start = time.time()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful translation assistant."},
                {"role": "user", "content": f"Translate this text to {target_language}:\n\n{text}"}
            ]
        )
        api_duration = time.time() - api_start
        
        translated_text = response.choices[0].message.content.strip()
        total_duration = time.time() - start_time
        
        logger.info(f"""
        Translation Performance Metrics:
        - Total time: {total_duration:.2f}s
        - OpenAI API time: {api_duration:.2f}s
        - Server processing time: {(total_duration - api_duration):.2f}s
        - Text length: {len(text)} chars
        """)
        
        return jsonify({'translatedText': translated_text})

    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        return jsonify({'error': str(e)}), 500

# Add this function to load the system prompt
def load_system_prompt(filename):
    prompt_path = Path(__file__).parent / filename
    try:
        with open(prompt_path, 'r') as file:
            return file.read().strip()
    except Exception as e:
        print(f"Error loading system prompt: {e}")
        return None

# Update the system prompt loading to include response format
QUALITY_CHECK_PROMPT = f"""
{load_system_prompt('system_prompt_qualityCheck.txt')}

IMPORTANT: Respond only in this JSON format:
{{
    "score": <overall_score_0_to_100>,
    "summary": "<brief_explanation>",
    "criteria": {{
        "clarity": <score_0_to_100>,
        "conciseness": <score_0_to_100>,
        "readability": <score_0_to_100>,
        "actionability": <score_0_to_100>,
        "toneConsistency": <score_0_to_100>,
        "brandFit": <score_0_to_100>
    }},
    "suggestions": [
        "<suggestion_1>",
        "<suggestion_2>",
        "<suggestion_3>"
    ]
}}
"""

@app.route('/quality-check', methods=['POST'])
def quality_check():
    try:
        data = request.json
        text = data.get('text', '')
        brand_guidelines = data.get('brandGuidelines', '')

        if not text:
            return jsonify({'error': 'No text provided'}), 400

        # Enhanced error handling for inputs
        if len(text) > 5000:  # Reasonable limit for API
            return jsonify({'error': 'Text too long. Maximum 5000 characters.'}), 400

        # Prepare the messages with better context
        messages = [
            {"role": "system", "content": QUALITY_CHECK_PROMPT},
            {"role": "user", "content": f"""
Text to evaluate:
{text}

Brand Guidelines:
{brand_guidelines if brand_guidelines else 'No specific brand guidelines provided.'}

Remember to respond only in the specified JSON format.
"""}
        ]

        # Call OpenAI with better error handling
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=1000,
                response_format={ "type": "json_object" }  # Ensure JSON response
            )
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            return jsonify({'error': 'Failed to process text. Please try again.'}), 500

        # Parse the response with better error handling
        try:
            response_text = response.choices[0].message.content
            response_data = json.loads(response_text)

            # Validate response structure
            required_fields = ['score', 'summary', 'criteria', 'suggestions']
            required_criteria = ['clarity', 'conciseness', 'readability', 
                               'actionability', 'toneConsistency', 'brandFit']

            # Check all required fields exist
            for field in required_fields:
                if field not in response_data:
                    raise ValueError(f"Missing required field: {field}")

            # Check all criteria exist
            for criterion in required_criteria:
                if criterion not in response_data['criteria']:
                    raise ValueError(f"Missing required criterion: {criterion}")

            # Validate score ranges
            if not (0 <= response_data['score'] <= 100):
                raise ValueError("Overall score out of range")

            for criterion, score in response_data['criteria'].items():
                if not (0 <= score <= 100):
                    raise ValueError(f"Criterion score out of range: {criterion}")

            # Ensure we have suggestions
            if not response_data['suggestions'] or len(response_data['suggestions']) < 1:
                response_data['suggestions'] = [
                    "Consider revising for clarity and conciseness.",
                    "Review the text for better alignment with brand guidelines.",
                    "Check readability and sentence structure."
                ]

            # Log successful analysis
            logger.info(f"Successfully analyzed text. Score: {response_data['score']}")

            return jsonify(response_data)

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse OpenAI response as JSON: {e}")
            return jsonify({'error': 'Invalid response format from analysis.'}), 500
        except ValueError as e:
            logger.error(f"Invalid response data: {e}")
            return jsonify({'error': str(e)}), 500
        except Exception as e:
            logger.error(f"Unexpected error processing response: {e}")
            return jsonify({'error': 'Failed to process analysis results.'}), 500

    except Exception as e:
        logger.error(f"Quality check error: {e}")
        return jsonify({
            'error': 'Failed to perform quality check. Please try again.',
            'details': str(e)
        }), 500

@app.route('/')
def home():
    return jsonify({'status': 'API is running'})

# Modify the after_request handler
@app.after_request
def after_request(response):
    origin = request.headers.get('Origin')
    if origin:  # Changed to handle any origin, will be filtered by CORS
        response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Accept'
    response.headers['Access-Control-Allow-Methods'] = 'POST,OPTIONS'
    return response

if __name__ == '__main__':
    logger.info("Starting server...")
    logger.info(f"OpenAI API key present: {'Yes' if os.getenv('OPENAI_API_KEY') else 'No'}")
    app.run(debug=True, port=5000)