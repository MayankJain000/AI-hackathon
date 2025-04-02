# AI-Powered Productivity Assistant with Emotional Intelligence

An innovative AI-powered productivity assistant that combines task management with emotional intelligence to create a more human-centric productivity solution. Built for the "AI for Productivity" hackathon, this assistant revolutionizes how we approach personal and team productivity by incorporating emotional awareness into task management.

## Features

### 🧠 Emotion-Aware Task Prioritization
- Real-time sentiment analysis of user inputs
- Dynamic task priority adjustment based on emotional state
- Stress-aware scheduling that automatically defers non-critical tasks
- Emotional state tracking and visualization

### 🌿 Smart Break Management
- AI-powered break scheduling based on stress levels and work patterns
- Personalized break recommendations including guided meditation and breathing exercises
- Break effectiveness tracking

### 📋 Intelligent Task Management
- Smart task organization and scheduling
- Priority-based task sorting
- Context-aware reminders

### 💪 Motivational Support System
- Personalized motivational messages based on emotional state
- Achievement celebration system
- Custom motivation strategies

### 👥 Team Emotional Intelligence
- Meeting sentiment analysis
- Team communication tone assessment
- Collaborative well-being tracking

## Technical Architecture

This project uses a FastAPI backend with various NLP components for sentiment analysis and Google's Gemini API for generating motivational content.

### Key Components:

- **Emotion Analyzer**: Detects and analyzes user emotional states
- **Task Prioritizer**: Adjusts task priorities based on emotional state
- **Motivational Generator**: Creates personalized motivational content using Google Gemini
- **REST API**: Exposes assistant capabilities to client applications

## Setup and Installation

### Prerequisites
- Python 3.9+
- Google Gemini API key (A default key is provided: `AIzaSyD2sEVrBWFCBRkp9jaFhAWUDKPm3A-fPMA`)

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-productivity-assistant.git
cd ai-productivity-assistant
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
# Edit .env if you want to use your own Gemini API key
```

### Running the Application

Start the FastAPI server:
```bash
python main.py
```

The API will be available at http://localhost:8000

API documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

- `POST /analyze` - Analyze user input text and emotional state
- `POST /task/complete` - Record a completed task
- `POST /break` - Record that user has taken a break
- `POST /team/analyze` - Analyze team sentiment from messages
- `GET /trends` - Get trends in user's emotional state
- `POST /reset` - Reset the assistant's state

## Usage Examples

### Analyze User Input

```python
import requests
import json

url = "http://localhost:8000/analyze"
data = {
    "text": "I'm really stressed about this deadline tomorrow!",
    "context": {
        "tasks": [
            {
                "id": "task1",
                "title": "Finish project presentation",
                "deadline": "2023-06-15T09:00:00",
                "importance": 0.9,
                "effort": 0.7,
                "estimated_minutes": 120
            },
            {
                "id": "task2",
                "title": "Reply to emails",
                "deadline": "2023-06-14T17:00:00",
                "importance": 0.5,
                "effort": 0.3,
                "estimated_minutes": 30
            }
        ]
    }
}

response = requests.post(url, json=data)
print(json.dumps(response.json(), indent=2))
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Google for Gemini API access
- Hugging Face for transformer models
- The open-source community for various tools and libraries

---
Built with ❤️ for the AI for Productivity Hackathon 