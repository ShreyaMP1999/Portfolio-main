from fastapi import APIRouter, HTTPException
from typing import List
from models.Experience import Experience, ExperienceCreate, ExperienceUpdate
from database import experience_collection
from datetime import datetime

router = APIRouter(prefix="/api/experience", tags=["experience"])

@router.get("/", response_model=List[Experience])
async def get_all_experiences():
    """Get all experience entries"""
    experiences = await experience_collection.find({"is_active": True}).sort("order", 1).to_list(1000)
    
    # Convert MongoDB _id to id
    for exp in experiences:
        exp["id"] = str(exp["_id"])
        del exp["_id"]
    
    return [Experience(**exp) for exp in experiences]

@router.post("/", response_model=Experience)
async def create_experience(experience: ExperienceCreate):
    """Create new experience entry"""
    experience_obj = Experience(**experience.dict())
    experience_dict = experience_obj.dict()
    experience_dict["_id"] = experience_dict["id"]
    del experience_dict["id"]
    
    await experience_collection.insert_one(experience_dict)
    return experience_obj

@router.put("/{experience_id}", response_model=Experience)
async def update_experience(experience_id: str, experience_update: ExperienceUpdate):
    """Update experience entry"""
    existing = await experience_collection.find_one({"_id": experience_id, "is_active": True})
    if not existing:
        raise HTTPException(status_code=404, detail="Experience not found")
    
    update_data = {k: v for k, v in experience_update.dict().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()
    
    await experience_collection.update_one(
        {"_id": experience_id},
        {"$set": update_data}
    )
    
    updated_exp = await experience_collection.find_one({"_id": experience_id})
    updated_exp["id"] = str(updated_exp["_id"])
    del updated_exp["_id"]
    
    return Experience(**updated_exp)

@router.delete("/{experience_id}")
async def delete_experience(experience_id: str):
    """Delete experience entry (soft delete)"""
    existing = await experience_collection.find_one({"_id": experience_id, "is_active": True})
    if not existing:
        raise HTTPException(status_code=404, detail="Experience not found")
    
    await experience_collection.update_one(
        {"_id": experience_id},
        {"$set": {"is_active": False, "updated_at": datetime.utcnow()}}
    )
    
    return {"message": "Experience deleted successfully"}