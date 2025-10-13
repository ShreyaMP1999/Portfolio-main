from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

class ProjectBase(BaseModel):
    title: str
    description: str
    long_description: str
    technologies: List[str]
    features: List[str]
    github: str
    demo: str
    image: str
    category: str
    order: int = 0

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    long_description: Optional[str] = None
    technologies: Optional[List[str]] = None
    features: Optional[List[str]] = None
    github: Optional[str] = None
    demo: Optional[str] = None
    image: Optional[str] = None
    category: Optional[str] = None
    order: Optional[int] = None

class Project(ProjectBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True