from fastapi import APIRouter, HTTPException
from typing import List
from models.PersonalInfo import PersonalInfo, PersonalInfoCreate, PersonalInfoUpdate
from database import personal_info_collection
from datetime import datetime

router = APIRouter(prefix="/api/personal", tags=["personal"])

@router.get("/", response_model=PersonalInfo)
async def get_personal_info():
    """Get personal information"""
    personal_info = await personal_info_collection.find_one({"is_active": True})
    if not personal_info:
        raise HTTPException(status_code=404, detail="Personal information not found")
    
    # Convert MongoDB _id to id
    personal_info["id"] = str(personal_info["_id"])
    del personal_info["_id"]
    
    return PersonalInfo(**personal_info)

@router.post("/", response_model=PersonalInfo)
async def create_personal_info(personal_info: PersonalInfoCreate):
    """Create personal information"""
    # Check if personal info already exists
    existing = await personal_info_collection.find_one({"is_active": True})
    if existing:
        raise HTTPException(status_code=400, detail="Personal information already exists. Use PUT to update.")
    
    personal_info_obj = PersonalInfo(**personal_info.dict())
    personal_info_dict = personal_info_obj.dict()
    personal_info_dict["_id"] = personal_info_dict["id"]
    del personal_info_dict["id"]
    
    await personal_info_collection.insert_one(personal_info_dict)
    return personal_info_obj

@router.put("/", response_model=PersonalInfo)
async def update_personal_info(personal_info_update: PersonalInfoUpdate):
    """Update personal information"""
    existing = await personal_info_collection.find_one({"is_active": True})
    if not existing:
        raise HTTPException(status_code=404, detail="Personal information not found")
    
    update_data = {k: v for k, v in personal_info_update.dict().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()
    
    await personal_info_collection.update_one(
        {"_id": existing["_id"]},
        {"$set": update_data}
    )
    
    updated_info = await personal_info_collection.find_one({"_id": existing["_id"]})
    updated_info["id"] = str(updated_info["_id"])
    del updated_info["_id"]
    
    return PersonalInfo(**updated_info)