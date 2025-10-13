from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

class ExperienceBase(BaseModel):
    company: str
    position: str
    duration: str
    location: str
    type: str
    responsibilities: List[str]
    technologies: List[str]
    order: int = 0

class ExperienceCreate(ExperienceBase):
    pass

class ExperienceUpdate(BaseModel):
    company: Optional[str] = None
    position: Optional[str] = None
    duration: Optional[str] = None
    location: Optional[str] = None
    type: Optional[str] = None
    responsibilities: Optional[List[str]] = None
    technologies: Optional[List[str]] = None
    order: Optional[int] = None

class Experience(ExperienceBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True