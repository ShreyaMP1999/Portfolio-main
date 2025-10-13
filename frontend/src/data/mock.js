// Mock data for Shreya's portfolio
export const personalInfo = {
  name: "Shreya Padaganur",
  title: "Full Stack Developer & AI/ML Engineer",
  location: "Chicago, Illinois",
  email: "shreyamp1999@gmail.com",
  phone: "+1 (312) 774-9512",
  linkedin: "https://www.linkedin.com/in/shreyamp/",
  github: "https://github.com/ShreyaMP1999",
  bio: "Passionate Full Stack Developer with 4+ years of experience in web development, AI/ML, and healthcare informatics. Currently pursuing MS in Computer Science at Illinois Institute of Technology with expertise in building scalable applications and intelligent systems.",
  tagline: "Building intelligent solutions that make a difference"
};

export const experience = [
  {
    id: 1,
    company: "Leap of Faith Technologies",
    position: "Software Development Consultant",
    duration: "May 2024 - August 2025",
    location: "Chicago, IL",
    type: "Contract",
    responsibilities: [
      "Developed a data extraction and reporting system for CMS MACRA/MIPS using ML models",
      "Improved NLP for better data extraction and analysis",
      "Built an automated reporting system to improve patient follow-ups",
      "Served as a Teaching Assistant for 'Digital Healthcare Informatics and AI'",
      "Led a team in developing an AI in Healthcare course"
    ],
    technologies: ["Python", "Machine Learning", "NLP", "Healthcare Analytics"]
  },
  {
    id: 2,
    company: "Accenture Solutions Pvt. Limited",
    position: "Full Stack Engineering Analyst",
    duration: "August 2021 - July 2023",
    location: "India",
    type: "Full-time",
    responsibilities: [
      "Spearheaded end-to-end web application development using front-end and back-end technologies",
      "Engineered enterprise applications on the Mendix platform",
      "Developed and deployed RESTful APIs",
      "Designed relational data models using Microsoft SQL Server Management Studio",
      "Investigated and debugged over 50 critical bugs and defects",
      "Implemented software development best practices"
    ],
    technologies: ["HTML", "CSS", "JavaScript", "C#", "Node.js", "Mendix", "SQL Server"]
  }
];

export const education = [
  {
    id: 1,
    degree: "Master of Science in Computer Science",
    school: "Illinois Institute of Technology",
    location: "Chicago, IL",
    duration: "2023 - May 2025",
    gpa: "3.5/4.0",
    relevant_courses: ["Digital Healthcare Informatics and AI", "Machine Learning", "Software Engineering"]
  },
  {
    id: 2,
    degree: "Bachelor of Engineering in Computer Science",
    school: "N. B. Navale Sinhgad College of Engineering",
    location: "India",
    duration: "2017 - May 2021",
    gpa: "3.8/4.0",
    achievements: ["Best Outgoing Student of the Year award (2020-21)", "President of Student Council (2019-20)"]
  }
];

export const projects = [
  {
    id: 1,
    title: "AI Chatbot for Mental Health Support",
    description: "An empathetic AI chatbot offering mental health support and resources, designed to provide accessible mental health assistance.",
    longDescription: "Developed a comprehensive mental health support chatbot using advanced NLP techniques. The chatbot provides empathetic responses, mental health resources, and stores user interaction data for analysis to improve support quality.",
    technologies: ["Python", "Flask", "HTML/CSS", "JavaScript", "OpenAI GPT API", "SQLite", "RESTful APIs"],
    features: [
      "Natural language processing for empathetic responses",
      "Mental health resource recommendations",
      "User interaction data analysis",
      "Secure conversation handling",
      "24/7 availability for support"
    ],
    github: "https://github.com/ShreyaMP1999/mental-health-chatbot",
    demo: "#",
    image: "/api/placeholder/600/400",
    category: "AI/ML"
  },
  {
    id: 2,
    title: "Personal Finance Tracker",
    description: "A comprehensive full-stack application for tracking personal finances with categorized transactions and monthly summaries.",
    longDescription: "Built a robust personal finance management system with secure user authentication, transaction categorization, and comprehensive reporting features. Deployed on AWS for scalability and reliability.",
    technologies: ["JavaScript", "React", "Node.js", "Express", "MongoDB", "RESTful APIs", "AWS"],
    features: [
      "Categorized transaction tracking",
      "Monthly financial summaries and analytics",
      "Secure user authentication and authorization",
      "Cloud-based data storage",
      "Responsive design for mobile and desktop",
      "Data visualization with charts and graphs"
    ],
    github: "https://github.com/ShreyaMP1999/finance-tracker",
    demo: "#",
    image: "/api/placeholder/600/400",
    category: "Full Stack"
  },
  {
    id: 3,
    title: "Intelligent Customer Support Chatbot",
    description: "An AI-powered customer support chatbot with advanced NLP capabilities for seamless customer interactions.",
    longDescription: "Developed an enterprise-grade customer support chatbot integrated with NLP using spaCy for natural language understanding. The system handles complex customer queries and provides intelligent responses.",
    technologies: ["Python", "Django", "React", "Node.js", "RESTful APIs", "AWS", "PostgreSQL", "spaCy", "NLP"],
    features: [
      "Advanced natural language processing",
      "Multi-intent recognition and handling",
      "Seamless integration with existing systems",
      "Real-time customer interaction",
      "Analytics and performance monitoring",
      "Scalable cloud deployment"
    ],
    github: "https://github.com/ShreyaMP1999/customer-support-bot",
    demo: "#",
    image: "/api/placeholder/600/400",
    category: "AI/ML"
  }
];

export const skills = {
  "Programming Languages": ["Java", "Python", "C", "C++", "JavaScript"],
  "Web Technologies": ["React", "Django", "Node.js", "Flask", "HTML", "CSS", "Express"],
  "Databases": ["MySQL", "PostgreSQL", "MongoDB", "SQLite", "Microsoft SQL Server"],
  "Cloud & DevOps": ["AWS", "Docker", "CI/CD", "Agile Methodologies"],
  "Tools & Platforms": ["Git", "GitHub", "Postman", "VS Code", "Eclipse", "Mendix"],
  "AI/ML & Data": ["Machine Learning", "NLP", "spaCy", "OpenAI GPT API", "Data Analysis"]
};

export const achievements = [
  {
    id: 1,
    title: "Vice President of DEI",
    organization: "Student Government Association, Illinois Institute of Technology",
    year: "2024-25",
    description: "Leading diversity, equity, and inclusion initiatives"
  },
  {
    id: 2,
    title: "Best Outgoing Student of the Year",
    organization: "N. B. Navale Sinhgad College of Engineering",
    year: "2020-21",
    description: "Recognized for academic excellence and leadership"
  },
  {
    id: 3,
    title: "Student Council President",
    organization: "NBNSCOE",
    year: "2019-20",
    description: "Elected to lead student body and represent student interests"
  }
];

export const socialLinks = [
  {
    name: "LinkedIn",
    url: "https://www.linkedin.com/in/shreyamp/", 
    icon: "linkedin"
  },
  {
    name: "GitHub",
    url: "https://github.com/ShreyaMP1999",
    icon: "github"
  },
  {
    name: "Email",
    url: "mailto:shreyamp1999@gmail.com",
    icon: "mail"
  }
];