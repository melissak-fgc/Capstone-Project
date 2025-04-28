import requests 
from flask import Flask, render_template, request

app = Flask(__name__)

def summarize_text(text):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3-8b-8192",
        "messages": [
            {"role": "user", "content": text}
        ],
        "temperature": 0.5
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Summarization failed."

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json.get('text')
    if not text:
        return {"error": "No text provided"}, 400
    summary = summarize_text(text)
    return {"summary": summary}

if __name__ == "__main__":
    app.run(debug=True)