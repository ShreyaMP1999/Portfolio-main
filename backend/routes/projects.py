from fastapi import APIRouter, HTTPException
from typing import List
from models.Project import Project, ProjectCreate, ProjectUpdate
from database import project_collection
from datetime import datetime

router = APIRouter(prefix="/api/projects", tags=["projects"])

@router.get("/", response_model=List[Project])
async def get_all_projects():
    """Get all projects"""
    projects = await project_collection.find({"is_active": True}).sort("order", 1).to_list(1000)
    
    # Convert MongoDB _id to id
    for project in projects:
        project["id"] = str(project["_id"])
        del project["_id"]
    
    return [Project(**project) for project in projects]

@router.get("/category/{category}", response_model=List[Project])
async def get_projects_by_category(category: str):
    """Get projects by category"""
    projects = await project_collection.find({"category": category, "is_active": True}).sort("order", 1).to_list(1000)
    
    # Convert MongoDB _id to id
    for project in projects:
        project["id"] = str(project["_id"])
        del project["_id"]
    
    return [Project(**project) for project in projects]

@router.post("/", response_model=Project)
async def create_project(project: ProjectCreate):
    """Create new project"""
    project_obj = Project(**project.dict())
    project_dict = project_obj.dict()
    project_dict["_id"] = project_dict["id"]
    del project_dict["id"]
    
    await project_collection.insert_one(project_dict)
    return project_obj

@router.put("/{project_id}", response_model=Project)
async def update_project(project_id: str, project_update: ProjectUpdate):
    """Update project"""
    existing = await project_collection.find_one({"_id": project_id, "is_active": True})
    if not existing:
        raise HTTPException(status_code=404, detail="Project not found")
    
    update_data = {k: v for k, v in project_update.dict().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()
    
    await project_collection.update_one(
        {"_id": project_id},
        {"$set": update_data}
    )
    
    updated_project = await project_collection.find_one({"_id": project_id})
    updated_project["id"] = str(updated_project["_id"])
    del updated_project["_id"]
    
    return Project(**updated_project)

@router.delete("/{project_id}")
async def delete_project(project_id: str):
    """Delete project (soft delete)"""
    existing = await project_collection.find_one({"_id": project_id, "is_active": True})
    if not existing:
        raise HTTPException(status_code=404, detail="Project not found")
    
    await project_collection.update_one(
        {"_id": project_id},
        {"$set": {"is_active": False, "updated_at": datetime.utcnow()}}
    )
    
    return {"message": "Project deleted successfully"}