from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

class SkillBase(BaseModel):
    category: str
    skills: List[str]
    order: int = 0

class SkillCreate(SkillBase):
    pass

class SkillUpdate(BaseModel):
    category: Optional[str] = None
    # skills: Optional[List[str]] = None
    order: Optional[int] = None

class Skill(SkillBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True