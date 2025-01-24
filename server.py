from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "your-openai-api-key"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return jsonify({"response": response['choices'][0]['message']['content']})

if __name__ == "__main__":
    app.run(port=5000)