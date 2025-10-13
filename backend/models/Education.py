from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

class EducationBase(BaseModel):
    degree: str
    school: str
    location: str
    duration: str
    gpa: str
    relevant_courses: Optional[List[str]] = []
    achievements: Optional[List[str]] = []
    order: int = 0

class EducationCreate(EducationBase):
    pass

class EducationUpdate(BaseModel):
    degree: Optional[str] = None
    school: Optional[str] = None
    location: Optional[str] = None
    duration: Optional[str] = None
    gpa: Optional[str] = None
    relevant_courses: Optional[List[str]] = None
    achievements: Optional[List[str]] = None
    order: Optional[int] = None

class Education(EducationBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True