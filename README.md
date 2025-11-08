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
