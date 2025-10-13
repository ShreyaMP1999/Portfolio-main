from fastapi import APIRouter, HTTPException
from typing import List
from models.ContactMessage import ContactMessage, ContactMessageCreate
from database import contact_message_collection

router = APIRouter(prefix="/api/contact", tags=["contact"])

@router.post("/", response_model=ContactMessage)
async def submit_contact_form(contact_message: ContactMessageCreate):
    """Submit contact form"""
    contact_obj = ContactMessage(**contact_message.dict())
    contact_dict = contact_obj.dict()
    contact_dict["_id"] = contact_dict["id"]
    del contact_dict["id"]
    
    await contact_message_collection.insert_one(contact_dict)
    return contact_obj

@router.get("/messages", response_model=List[ContactMessage])
async def get_all_contact_messages():
    """Get all contact messages (admin only)"""
    messages = await contact_message_collection.find().sort("created_at", -1).to_list(1000)
    
    # Convert MongoDB _id to id
    for message in messages:
        message["id"] = str(message["_id"])
        del message["_id"]
    
    return [ContactMessage(**message) for message in messages]

@router.put("/messages/{message_id}/read")
async def mark_message_as_read(message_id: str):
    """Mark contact message as read"""
    existing = await contact_message_collection.find_one({"_id": message_id})
    if not existing:
        raise HTTPException(status_code=404, detail="Message not found")
    
    await contact_message_collection.update_one(
        {"_id": message_id},
        {"$set": {"is_read": True}}
    )
    
    return {"message": "Message marked as read"}