from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
database_name = os.environ.get('DB_NAME', 'portfolio_db')

client = AsyncIOMotorClient(mongo_url)
db = client[database_name]

# Collections
personal_info_collection = db.personal_info
experience_collection = db.experience
project_collection = db.projects
skill_collection = db.skills
achievement_collection = db.achievements
education_collection = db.education
contact_message_collection = db.contact_messages

async def close_db_connection():
    client.close()