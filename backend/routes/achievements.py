from fastapi import APIRouter, HTTPException
from typing import List
from models.Achievement import Achievement, AchievementCreate, AchievementUpdate
from database import achievement_collection
from datetime import datetime

router = APIRouter(prefix="/api/achievements", tags=["achievements"])

@router.get("/", response_model=List[Achievement])
async def get_all_achievements():
    """Get all achievements"""
    achievements = await achievement_collection.find({"is_active": True}).sort("order", 1).to_list(1000)
    
    # Convert MongoDB _id to id
    for achievement in achievements:
        achievement["id"] = str(achievement["_id"])
        del achievement["_id"]
    
    return [Achievement(**achievement) for achievement in achievements]

@router.post("/", response_model=Achievement)
async def create_achievement(achievement: AchievementCreate):
    """Create new achievement"""
    achievement_obj = Achievement(**achievement.dict())
    achievement_dict = achievement_obj.dict()
    achievement_dict["_id"] = achievement_dict["id"]
    del achievement_dict["id"]
    
    await achievement_collection.insert_one(achievement_dict)
    return achievement_obj

@router.put("/{achievement_id}", response_model=Achievement)
async def update_achievement(achievement_id: str, achievement_update: AchievementUpdate):
    """Update achievement"""
    existing = await achievement_collection.find_one({"_id": achievement_id, "is_active": True})
    if not existing:
        raise HTTPException(status_code=404, detail="Achievement not found")
    
    update_data = {k: v for k, v in achievement_update.dict().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()
    
    await achievement_collection.update_one(
        {"_id": achievement_id},
        {"$set": update_data}
    )
    
    updated_achievement = await achievement_collection.find_one({"_id": achievement_id})
    updated_achievement["id"] = str(updated_achievement["_id"])
    del updated_achievement["_id"]
    
    return Achievement(**updated_achievement)

@router.delete("/{achievement_id}")
async def delete_achievement(achievement_id: str):
    """Delete achievement (soft delete)"""
    existing = await achievement_collection.find_one({"_id": achievement_id, "is_active": True})
    if not existing:
        raise HTTPException(status_code=404, detail="Achievement not found")
    
    await achievement_collection.update_one(
        {"_id": achievement_id},
        {"$set": {"is_active": False, "updated_at": datetime.utcnow()}}
    )
    
    return {"message": "Achievement deleted successfully"}