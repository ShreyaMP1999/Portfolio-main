from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

class PersonalInfoBase(BaseModel):
    name: str
    title: str
    location: str
    email: str
    phone: str
    linkedin: str
    github: str
    bio: str
    tagline: str

class PersonalInfoCreate(PersonalInfoBase):
    pass

class PersonalInfoUpdate(BaseModel):
    name: Optional[str] = None
    title: Optional[str] = None
    location: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    bio: Optional[str] = None
    tagline: Optional[str] = None

class PersonalInfo(PersonalInfoBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True