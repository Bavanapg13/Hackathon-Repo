# Placeholder module for Pydantic schemas
# Expand with real request/response models as the API grows
from pydantic import BaseModel

class HealthCheck(BaseModel):
    status: str
