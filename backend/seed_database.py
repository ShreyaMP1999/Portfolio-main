import asyncio
from database import (
    personal_info_collection, experience_collection, project_collection,
    skill_collection, achievement_collection, education_collection
)
from models.PersonalInfo import PersonalInfo
from models.Experience import Experience
from models.Project import Project
from models.Skill import Skill
from models.Achievement import Achievement
from models.Education import Education

# Mock data from frontend
mock_personal_info = {
    "name": "Shreya Padaganur",
    "title": "Full Stack Developer & AI/ML Engineer",
    "location": "Chicago, Illinois",
    "email": "shreyamp1999@gmail.com",
    "phone": "+1 (312) 774-9512",
    "linkedin": "https://www.linkedin.com/in/shreyamp/",
    "github": "https://github.com/ShreyaMP1999",
    "bio": "Passionate Full Stack Developer with 4+ years of experience in web development, AI/ML, and healthcare informatics. Currently pursuing MS in Computer Science at Illinois Institute of Technology with expertise in building scalable applications and intelligent systems.",
    "tagline": "Building intelligent solutions that make a difference"
}

mock_experience = [
    {
        "company": "Leap of Faith Technologies",
        "position": "Software Development Consultant",
        "duration": "May 2024 - August 2025",
        "location": "Chicago, IL",
        "type": "Contract",
        "responsibilities": [
            "Developed a data extraction and reporting system for CMS MACRA/MIPS using ML models",
            "Improved NLP for better data extraction and analysis",
            "Built an automated reporting system to improve patient follow-ups",
            "Served as a Teaching Assistant for 'Digital Healthcare Informatics and AI'",
            "Led a team in developing an AI in Healthcare course"
        ],
        "technologies": ["Python", "Machine Learning", "NLP", "Healthcare Analytics"],
        "order": 1
    },
    {
        "company": "Accenture Solutions Pvt. Limited",
        "position": "Full Stack Engineering Analyst",
        "duration": "August 2021 - July 2023",
        "location": "India",
        "type": "Full-time",
        "responsibilities": [
            "Spearheaded end-to-end web application development using front-end and back-end technologies",
            "Engineered enterprise applications on the Mendix platform",
            "Developed and deployed RESTful APIs",
            "Designed relational data models using Microsoft SQL Server Management Studio",
            "Investigated and debugged over 50 critical bugs and defects",
            "Implemented software development best practices"
        ],
        "technologies": ["HTML", "CSS", "JavaScript", "C#", "Node.js", "Mendix", "SQL Server"],
        "order": 2
    }
]

mock_education = [
    {
        "degree": "Master of Science in Computer Science",
        "school": "Illinois Institute of Technology",
        "location": "Chicago, IL",
        "duration": "2023 - May 2025",
        "gpa": "3.5/4.0",
        "relevant_courses": ["Digital Healthcare Informatics and AI", "Machine Learning", "Software Engineering"],
        "achievements": [],
        "order": 1
    },
    {
        "degree": "Bachelor of Engineering in Computer Science",
        "school": "N. B. Navale Sinhgad College of Engineering",
        "location": "India",
        "duration": "2017 - May 2021",
        "gpa": "3.8/4.0",
        "relevant_courses": [],
        "achievements": ["Best Outgoing Student of the Year award (2020-21)", "President of Student Council (2019-20)"],
        "order": 2
    }
]

mock_projects = [
    {
        "title": "AI Chatbot for Mental Health Support",
        "description": "An empathetic AI chatbot offering mental health support and resources, designed to provide accessible mental health assistance.",
        "long_description": "Developed a comprehensive mental health support chatbot using advanced NLP techniques. The chatbot provides empathetic responses, mental health resources, and stores user interaction data for analysis to improve support quality.",
        "technologies": ["Python", "Flask", "HTML/CSS", "JavaScript", "OpenAI GPT API", "SQLite", "RESTful APIs"],
        "features": [
            "Natural language processing for empathetic responses",
            "Mental health resource recommendations",
            "User interaction data analysis",
            "Secure conversation handling",
            "24/7 availability for support"
        ],
        "github": "https://github.com/ShreyaMP1999/mental-health-chatbot",
        "demo": "#",
        "image": "/api/placeholder/600/400",
        "category": "AI/ML",
        "order": 1
    },
    {
        "title": "Personal Finance Tracker",
        "description": "A comprehensive full-stack application for tracking personal finances with categorized transactions and monthly summaries.",
        "long_description": "Built a robust personal finance management system with secure user authentication, transaction categorization, and comprehensive reporting features. Deployed on AWS for scalability and reliability.",
        "technologies": ["JavaScript", "React", "Node.js", "Express", "MongoDB", "RESTful APIs", "AWS"],
        "features": [
            "Categorized transaction tracking",
            "Monthly financial summaries and analytics",
            "Secure user authentication and authorization",
            "Cloud-based data storage",
            "Responsive design for mobile and desktop",
            "Data visualization with charts and graphs"
        ],
        "github": "https://github.com/ShreyaMP1999/finance-tracker",
        "demo": "#",
        "image": "/api/placeholder/600/400",
        "category": "Full Stack",
        "order": 2
    },
    {
        "title": "Intelligent Customer Support Chatbot",
        "description": "An AI-powered customer support chatbot with advanced NLP capabilities for seamless customer interactions.",
        "long_description": "Developed an enterprise-grade customer support chatbot integrated with NLP using spaCy for natural language understanding. The system handles complex customer queries and provides intelligent responses.",
        "technologies": ["Python", "Django", "React", "Node.js", "RESTful APIs", "AWS", "PostgreSQL", "spaCy", "NLP"],
        "features": [
            "Advanced natural language processing",
            "Multi-intent recognition and handling",
            "Seamless integration with existing systems",
            "Real-time customer interaction",
            "Analytics and performance monitoring",
            "Scalable cloud deployment"
        ],
        "github": "https://github.com/ShreyaMP1999/customer-support-bot",
        "demo": "#",
        "image": "/api/placeholder/600/400",
        "category": "AI/ML",
        "order": 3
    }
]

mock_skills = [
    {"category": "Programming Languages", "skills": ["Java", "Python", "C", "C++", "JavaScript"], "order": 1},
    {"category": "Web Technologies", "skills": ["React", "Django", "Node.js", "Flask", "HTML", "CSS", "Express"], "order": 2},
    {"category": "Databases", "skills": ["MySQL", "PostgreSQL", "MongoDB", "SQLite", "Microsoft SQL Server"], "order": 3},
    {"category": "Cloud & DevOps", "skills": ["AWS", "Docker", "CI/CD", "Agile Methodologies"], "order": 4},
    {"category": "Tools & Platforms", "skills": ["Git", "GitHub", "Postman", "VS Code", "Eclipse", "Mendix"], "order": 5},
    {"category": "AI/ML & Data", "skills": ["Machine Learning", "NLP", "spaCy", "OpenAI GPT API", "Data Analysis"], "order": 6}
]

mock_achievements = [
    {
        "title": "Vice President of DEI",
        "organization": "Student Government Association, Illinois Institute of Technology",
        "year": "2024-25",
        "description": "Leading diversity, equity, and inclusion initiatives",
        "order": 1
    },
    {
        "title": "Best Outgoing Student of the Year",
        "organization": "N. B. Navale Sinhgad College of Engineering",
        "year": "2020-21",
        "description": "Recognized for academic excellence and leadership",
        "order": 2
    },
    {
        "title": "Student Council President",
        "organization": "NBNSCOE",
        "year": "2019-20",
        "description": "Elected to lead student body and represent student interests",
        "order": 3
    }
]

async def seed_database():
    """Seed the database with initial data"""
    print("Starting database seeding...")
    
    # Clear existing data
    await personal_info_collection.delete_many({})
    await experience_collection.delete_many({})
    await project_collection.delete_many({})
    await skill_collection.delete_many({})
    await achievement_collection.delete_many({})
    await education_collection.delete_many({})
    
    print("Cleared existing data")
    
    # Seed personal info
    personal_info_obj = PersonalInfo(**mock_personal_info)
    personal_info_dict = personal_info_obj.dict()
    personal_info_dict["_id"] = personal_info_dict["id"]
    del personal_info_dict["id"]
    await personal_info_collection.insert_one(personal_info_dict)
    print("Seeded personal info")
    
    # Seed experience
    for exp_data in mock_experience:
        experience_obj = Experience(**exp_data)
        experience_dict = experience_obj.dict()
        experience_dict["_id"] = experience_dict["id"]
        del experience_dict["id"]
        await experience_collection.insert_one(experience_dict)
    print("Seeded experience data")
    
    # Seed education
    for edu_data in mock_education:
        education_obj = Education(**edu_data)
        education_dict = education_obj.dict()
        education_dict["_id"] = education_dict["id"]
        del education_dict["id"]
        await education_collection.insert_one(education_dict)
    print("Seeded education data")
    
    # Seed projects
    for project_data in mock_projects:
        project_obj = Project(**project_data)
        project_dict = project_obj.dict()
        project_dict["_id"] = project_dict["id"]
        del project_dict["id"]
        await project_collection.insert_one(project_dict)
    print("Seeded projects data")
    
    # Seed skills
    for skill_data in mock_skills:
        skill_obj = Skill(**skill_data)
        skill_dict = skill_obj.dict()
        skill_dict["_id"] = skill_dict["id"]
        del skill_dict["id"]
        await skill_collection.insert_one(skill_dict)
    print("Seeded skills data")
    
    # Seed achievements
    for achievement_data in mock_achievements:
        achievement_obj = Achievement(**achievement_data)
        achievement_dict = achievement_obj.dict()
        achievement_dict["_id"] = achievement_dict["id"]
        del achievement_dict["id"]
        await achievement_collection.insert_one(achievement_dict)
    print("Seeded achievements data")
    
    print("Database seeding completed successfully!")

if __name__ == "__main__":
    asyncio.run(seed_database())