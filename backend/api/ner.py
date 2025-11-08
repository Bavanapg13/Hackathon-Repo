from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from ..models.ner_model import get_model

router = APIRouter()

class NERRequest(BaseModel):
    text: str

class Entity(BaseModel):
    text: str
    label: str
    start: int
    end: int

class NERResponse(BaseModel):
    entities: List[Entity]

@router.post("/extract", response_model=NERResponse)
async def extract_entities(req: NERRequest):
    model = get_model()
    try:
        entities = model.extract(req.text)
        return {"entities": entities}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
