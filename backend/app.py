from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import auth, tasks, ner

app = FastAPI(title="Hackathon NER API")

# Allow common CORS from frontend during local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])
app.include_router(ner.router, prefix="/api/ner", tags=["ner"])

@app.get("/")
async def root():
    return {"message": "Hackathon NER API is running"}
