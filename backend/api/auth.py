from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import timedelta

from ..core import security

router = APIRouter()

# In-memory user store (replace with DB in production)
_users = {}

class RegisterRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/register", response_model=dict)
async def register(req: RegisterRequest):
    if req.username in _users:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed = security.hash_password(req.password)
    _users[req.username] = {"username": req.username, "password": hashed}
    return {"message": "registered"}

@router.post("/login", response_model=TokenResponse)
async def login(req: LoginRequest):
    user = _users.get(req.username)
    if not user or not security.verify_password(req.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=60)
    token = security.create_access_token({"sub": req.username}, expires_delta=access_token_expires)
    return {"access_token": token, "token_type": "bearer"}
