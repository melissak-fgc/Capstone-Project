import requests 
from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file uploaded')
            return render_template('upload.html')
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return render_template('upload.html')
        
        if file and file.filename.endswith('.txt'):
            text = file.read().decode('utf-8')
            summary = summarize_text(text)
            return render_template('upload.html', original_text=text, summarized_text=summary)
        else:
            flash('Please upload a .txt file')
            return render_template('upload.html')
    
    return render_template('upload.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json.get('text')
    if not text:
        return {"error": "No text provided"}, 400
    summary = summarize_text(text)
    return {"summary": summary}

if __name__ == "__main__":
    app.run(debug=True)