from fastapi import APIRouter, HTTPException
from typing import List
from models.Skill import Skill, SkillCreate, SkillUpdate
from database import skill_collection
from datetime import datetime

router = APIRouter(prefix="/api/skills", tags=["skills"])

@router.get("/", response_model=List[Skill])
async def get_all_skills():
    """Get all skills by categories."""
    # skills = await skill_collection.find({"is_active": True}).sort("order", 1).to_list(1000)
    skills = await skill_collection.find({"is_active": True}).sort("order", 1).to_list(1000)

    # Convert MongoDB _id to id
    for skill in skills:
        skill["id"] = str(skill["_id"])
        del skill["_id"]
    
    return [Skill(**skill) for skill in skills]

@router.post("/", response_model=Skill)
async def create_skill_category(skill: SkillCreate):
    """Create new skill category"""
    skill_obj = Skill(**skill.dict())
    skill_dict = skill_obj.dict()
    skill_dict["_id"] = skill_dict["id"]
    del skill_dict["id"]
    
    await skill_collection.insert_one(skill_dict)
    return skill_obj

@router.put("/{skill_id}", response_model=Skill)
async def update_skill_category(skill_id: str, skill_update: SkillUpdate):
    """Update skill category"""
    existing = await skill_collection.find_one({"_id": skill_id, "is_active": True})
    if not existing:
        raise HTTPException(status_code=404, detail="Skill category not found")
    
    update_data = {k: v for k, v in skill_update.dict().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()
    
    await skill_collection.update_one(
        {"_id": skill_id},
        {"$set": update_data}
    )
    
    updated_skill = await skill_collection.find_one({"_id": skill_id})
    updated_skill["id"] = str(updated_skill["_id"])
    del updated_skill["_id"]
    
    return Skill(**updated_skill)

@router.delete("/{skill_id}")
async def delete_skill_category(skill_id: str):
    """Delete skill category (soft delete)"""
    existing = await skill_collection.find_one({"_id": skill_id, "is_active": True})
    if not existing:
        raise HTTPException(status_code=404, detail="Skill category not found")
    
    await skill_collection.update_one(
        {"_id": skill_id},
        {"$set": {"is_active": False, "updated_at": datetime.utcnow()}}
    )
    
    return {"message": "Skill category deleted successfully"}