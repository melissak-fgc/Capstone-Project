# AI-Powered Text Summarizer Web Application

## Overview
This web application leverages artificial intelligence to automatically generate concise summaries of text content. It provides an intuitive interface for users to input text and receive AI-generated summaries, making it easier to extract key information from lengthy documents.

## Features
- 📝 Text input through direct typing or file upload
- 🤖 AI-powered summarization using advanced language models
- ⚡ Real-time processing and instant results
- 📊 Adjustable summary length options
- 📱 Responsive design for desktop and mobile devices
- 🔒 Secure text processing with privacy considerations

## Tech Stack
- Frontend: React.js with TypeScript
- Backend: Python with FastAPI
- AI Model: OpenAI GPT API or Groq API
- Styling: Tailwind CSS
- Deployment: Docker containerization

## Getting Started

### Prerequisites
- Node.js (v16 or higher)
- Python (v3.8 or higher)
- OpenAI API key or Groq API key (Groq is compatible with OpenAI's API)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/Capstone-Project.git
cd Capstone-Project
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

3. Install backend dependencies:
```bash
cd ../backend
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Add your OpenAI API key to .env
```

### Running the Application
1. Start the backend server:
```bash
cd backend
uvicorn main:app --reload
```

2. Start the frontend development server:
```bash
cd frontend
npm run dev
```

3. Open your browser and navigate to `http://localhost:3000`

## Usage
1. Enter or paste your text in the input area
2. Select your desired summary length
3. Click "Summarize" to generate the summary
4. View and copy your generated summary

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- OpenAI for providing the GPT API
- All contributors who have helped shape this project

## Contact
For any questions or feedback, please open an issue in the repository.
