<<<<<<< HEAD
# Hackathon-Repo

Full-stack application with FastAPI backend (NER model) and React frontend. Supports both Docker and local development workflows.

## Quick Start with Docker (Recommended)

The easiest way to run the entire application:

```bash
# Build and start all services
docker-compose up --build

# Access the applications:
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Documentation: http://localhost:8000/docs
```

## Manual Setup (Development)

### Backend Setup

1. Create and activate a Python virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Unix/macOS
python3 -m venv .venv
source .venv/bin/activate
```

2. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Run the backend server:
```bash
# From the backend directory
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

1. Install Node.js dependencies:
```bash
cd frontend
npm install
```

2. Start the development server:
```bash
# Set API base URL and start
$env:REACT_APP_API_BASE='http://localhost:8000/api'  # Windows
export REACT_APP_API_BASE='http://localhost:8000/api' # Unix/macOS
npm run dev
```

The frontend will be available at http://localhost:3000

## API Documentation

- Interactive API docs (Swagger UI): http://localhost:8000/docs
- ReDoc alternative docs: http://localhost:8000/redoc

## Available Endpoints

Backend API endpoints:

- POST `/api/auth/register` - Create new user account
- POST `/api/auth/login` - Login and get JWT token
- POST `/api/ner/extract` - Extract entities from text
- GET/POST `/api/tasks` - Task CRUD operations

## Development Notes

- The NER implementation in `backend/models/ner_model.py` is currently a stub; replace with a proper transformers pipeline for production use.
- Authentication uses an in-memory store and a placeholder secret — replace with a database and secure key for production.
- Hot reload is enabled for both frontend and backend in development mode.
- API base URL defaults to http://localhost:8000/api but can be configured via REACT_APP_API_BASE environment variable.
=======
# 🍕 Named Entity Recognition System for Domino's Texts
Fine-tuned transformer-based model that extracts order details like size, item, topping, address, and time from text.

## How It Works
1. The NER model (DistilBERT) is fine-tuned using Hugging Face Transformers.
2. FastAPI serves the model as a REST API.
3. Frontend (HTML, CSS, JS) sends text → API returns entities → UI displays results.

## Run Steps
```bash
pip install -r backend/requirements.txt
python train_ner.py
cd backend
uvicorn app:app --reload
>>>>>>> f16879b4c6341ce558b4653dc33f0f1a51e6bdbf
