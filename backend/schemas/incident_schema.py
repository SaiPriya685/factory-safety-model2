from pydantic import BaseModel
from datetime import datetime


class IncidentResponse(BaseModel):

    id: int

    violation: str

    severity: str

    location: str

    created_at: datetime


    class Config:
        from_attributes = True