# AI-Interviewer-BACKEND-HCI

AI-Interviewer-BACKEND-HCI is a backend service for an AI-based interviewing platform, leveraging FastAPI and other technologies to provide an interactive interview experience.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python
- pip (Python package manager)

### Environment Setup

To set up the project environment:

1. **Create a Virtual Environment and**:

- python3 -m venv your-env-name
- source your-env-name/bin/activate
- pip3 install -r requirements.txt

2. **Running the Project**:
- uvicorn main:app --reload

2. **You should create a .env file locally which contains ELEVENLABS_KEY, OPEN_AI_KEY, and OPEN_AI_ORG**

### Other
The project will be available at: http://localhost:8000

For API documentation and testing, visit: http://localhost:8000/docs

Data Storage:
Dialogue text information is stored in database.json.
Please ensure to clear the database.json before each test.
Configurations:
The load_messages function defines the persona for the Chatbot.
In the text_to_speech function, voice_id specifies the voice style for responses. For more details on voice styles, visit ElevenLabs API Reference.
Interface Testing:
Record Audio: Use Vocaroo to create audio recordings for testing.
Upload and Test: Use Postman to upload audio files and test the API.



