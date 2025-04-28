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
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": f"Please summarize the following text: {text}"}
        ],
        "temperature": 0.5
    }
    try:
        print("Making API request to Groq...")
        print(f"Request URL: {url}")
        print(f"Request Headers: {headers}")
        print(f"Request Data: {data}")
        
        response = requests.post(url, headers=headers, json=data)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Body: {response.text}")
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            error_message = f"API Error: Status code {response.status_code}, Response: {response.text}"
            print(error_message)
            return f"Summarization failed. {error_message}"
    except Exception as e:
        error_message = f"Error: {str(e)}"
        print(error_message)
        return f"Summarization failed. {error_message}"

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