from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

class AchievementBase(BaseModel):
    title: str
    organization: str
    year: str
    description: str
    order: int = 0

class AchievementCreate(AchievementBase):
    pass

class AchievementUpdate(BaseModel):
    title: Optional[str] = None
    organization: Optional[str] = None
    year: Optional[str] = None
    description: Optional[str] = None
    order: Optional[int] = None

class Achievement(AchievementBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True