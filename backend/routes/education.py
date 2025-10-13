from fastapi import APIRouter, HTTPException
from typing import List
from models.Education import Education, EducationCreate, EducationUpdate
from database import education_collection
from datetime import datetime

router = APIRouter(prefix="/api/education", tags=["education"])

@router.get("/", response_model=List[Education])
async def get_all_education():
    """Get all education entries"""
    education_entries = await education_collection.find({"is_active": True}).sort("order", 1).to_list(1000)
    
    # Convert MongoDB _id to id
    for edu in education_entries:
        edu["id"] = str(edu["_id"])
        del edu["_id"]
    
    return [Education(**edu) for edu in education_entries]

@router.post("/", response_model=Education)
async def create_education(education: EducationCreate):
    """Create new education entry"""
    education_obj = Education(**education.dict())
    education_dict = education_obj.dict()
    education_dict["_id"] = education_dict["id"]
    del education_dict["id"]
    
    await education_collection.insert_one(education_dict)
    return education_obj

@router.put("/{education_id}", response_model=Education)
async def update_education(education_id: str, education_update: EducationUpdate):
    """Update education entry"""
    existing = await education_collection.find_one({"_id": education_id, "is_active": True})
    if not existing:
        raise HTTPException(status_code=404, detail="Education entry not found")
    
    update_data = {k: v for k, v in education_update.dict().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()
    
    await education_collection.update_one(
        {"_id": education_id},
        {"$set": update_data}
    )
    
    updated_education = await education_collection.find_one({"_id": education_id})
    updated_education["id"] = str(updated_education["_id"])
    del updated_education["_id"]
    
    return Education(**updated_education)

@router.delete("/{education_id}")
async def delete_education(education_id: str):
    """Delete education entry (soft delete)"""
    existing = await education_collection.find_one({"_id": education_id, "is_active": True})
    if not existing:
        raise HTTPException(status_code=404, detail="Education entry not found")
    
    await education_collection.update_one(
        {"_id": education_id},
        {"$set": {"is_active": False, "updated_at": datetime.utcnow()}}
    )
    
    return {"message": "Education entry deleted successfully"}