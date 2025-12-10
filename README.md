# Shreya Padaganur - Full Stack Portfolio Website

A modern, dynamic, and responsive portfolio website showcasing my journey as a Full Stack Developer and AI/ML Engineer. Built with cutting-edge technologies and featuring a complete backend API for dynamic content management.

<!-- ![Portfolio Preview](https://via.placeholder.com/800x400/2563eb/ffffff?text=Portfolio+Website+Preview)

## 🌟 Live Demo

- **Live Website**: [Your Portfolio URL]
- **API Documentation**: [Your API URL]/docs

## 📋 Table of Contents

- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Setup](#environment-setup)
  - [Running the Application](#running-the-application)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## ✨ Features

### 🎨 Frontend Features
- **Modern Design**: Clean, professional, and responsive design following current UI/UX trends
- **Interactive Navigation**: Smooth scrolling navigation with animated sections
- **Dynamic Content**: Real-time data loading from backend APIs
- **Loading States**: Professional loading indicators and skeleton screens
- **Error Handling**: Graceful error states with retry functionality
- **Contact Form**: Functional contact form with backend integration
- **Mobile Responsive**: Optimized for all device sizes
- **Professional Animations**: Hover effects, transitions, and micro-interactions

### 🔧 Backend Features
- **RESTful APIs**: Complete CRUD operations for all portfolio sections
- **Data Management**: MongoDB integration for dynamic content storage
- **Contact Management**: Contact form submissions stored in database
- **Error Handling**: Comprehensive error responses and validation
- **CORS Support**: Proper cross-origin resource sharing configuration
- **API Documentation**: Auto-generated API documentation with FastAPI

### 📱 Sections
- **Hero Section**: Dynamic introduction with personal information
- **About**: Professional bio, achievements, and statistics
- **Experience**: Work history with detailed responsibilities and technologies
- **Projects**: Featured projects with categories, technologies, and links
- **Skills**: Categorized technical skills and competencies
- **Education**: Academic background and achievements
- **Contact**: Working contact form with message storage

## 🛠 Technologies Used

### Frontend
- **React** (v19.0.0) - Modern JavaScript library for building user interfaces
- **Tailwind CSS** (v3.4.17) - Utility-first CSS framework for rapid UI development
- **shadcn/ui** - High-quality, accessible React component library
- **Lucide React** - Beautiful, customizable SVG icons
- **Axios** - Promise-based HTTP client for API requests
- **React Router Dom** (v7.5.1) - Declarative routing for React applications

### Backend
- **FastAPI** (v0.110.1) - Modern, fast web framework for building APIs with Python
- **MongoDB** with **Motor** (v3.3.1) - Async MongoDB driver for Python
- **Pydantic** (v2.6.4+) - Data validation using Python type annotations
- **Python** (3.8+) - Core programming language
- **CORS Middleware** - Cross-origin resource sharing support

### Development & Deployment
- **Docker** - Containerization for consistent development environments
- **Supervisor** - Process management for running multiple services
- **Git** - Version control system
- **ESLint** - JavaScript/TypeScript linting
- **Craco** - Create React App Configuration Override

## 🚀 Getting Started

### Prerequisites

Before running this project, make sure you have the following installed:

- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **MongoDB** (v4.4 or higher)
- **Yarn** (recommended) or npm
- **Git**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShreyaMP1999/portfolio-website.git
   cd portfolio-website
   ```

2. **Install Frontend Dependencies**
   ```bash
   cd frontend
   yarn install
   # or
   npm install
   ```

3. **Install Backend Dependencies**
   ```bash
   cd ../backend
   pip install -r requirements.txt
   ```

### Environment Setup

1. **Backend Environment Variables**
   
   Create a `.env` file in the `backend` directory:
   ```env
   MONGO_URL=mongodb://localhost:27017
   DB_NAME=portfolio_db
   ```

2. **Frontend Environment Variables**
   
   Create a `.env` file in the `frontend` directory:
   ```env
   REACT_APP_BACKEND_URL=http://localhost:8001
   ```

### Running the Application

#### Method 1: Using Supervisor (Recommended)

1. **Start all services**
   ```bash
   sudo supervisorctl start all
   ```

2. **Check service status**
   ```bash
   sudo supervisorctl status
   ```

#### Method 2: Manual Setup

1. **Start MongoDB**
   ```bash
   sudo systemctl start mongod
   ```

2. **Seed the Database**
   ```bash
   cd backend
   python seed_database.py
   ```

3. **Start Backend Server**
   ```bash
   cd backend
   uvicorn server:app --host 0.0.0.0 --port 8001 --reload
   ```

4. **Start Frontend Development Server**
   ```bash
   cd frontend
   yarn start
   # or
   npm start
   ```

5. **Access the Application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8001
   - API Documentation: http://localhost:8001/docs

## 📖 Usage

### Viewing the Portfolio
Simply navigate to `http://localhost:3000` to view the complete portfolio website with all sections populated with real data from the backend.

### API Endpoints
The backend provides RESTful APIs for managing portfolio content:

- **Personal Info**: `GET/PUT /api/personal/`
- **Experience**: `GET/POST/PUT/DELETE /api/experience/`
- **Projects**: `GET/POST/PUT/DELETE /api/projects/`
- **Skills**: `GET/POST/PUT/DELETE /api/skills/`
- **Achievements**: `GET/POST/PUT/DELETE /api/achievements/`
- **Education**: `GET/POST/PUT/DELETE /api/education/`
- **Contact**: `POST /api/contact/`

### Adding New Content
Use the API endpoints to add new projects, experiences, or skills:

```python
# Example: Adding a new project
import requests

project_data = {
    "title": "New Amazing Project",
    "description": "A brief description of the project",
    "technologies": ["React", "Python", "MongoDB"],
    "github": "https://github.com/username/project",
    "demo": "https://project-demo.com",
    "category": "Full Stack"
}

response = requests.post("http://localhost:8001/api/projects/", json=project_data)
```

## 📚 API Documentation

The complete API documentation is automatically generated and available at:
- **Swagger UI**: http://localhost:8001/docs
- **ReDoc**: http://localhost:8001/redoc

## 📁 Project Structure

```
portfolio-website/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── ui/          # shadcn/ui components
│   │   │   ├── About.jsx
│   │   │   ├── Contact.jsx
│   │   │   ├── Experience.jsx
│   │   │   ├── Header.jsx
│   │   │   ├── Hero.jsx
│   │   │   ├── Projects.jsx
│   │   │   └── Skills.jsx
│   │   ├── services/        # API service layer
│   │   │   └── api.js
│   │   ├── hooks/           # Custom React hooks
│   │   │   └── useApi.js
│   │   ├── App.js           # Main App component
│   │   └── index.js         # Entry point
│   ├── package.json
│   └── tailwind.config.js
├── backend/                  # FastAPI backend application
│   ├── models/              # Pydantic models
│   │   ├── PersonalInfo.py
│   │   ├── Experience.py
│   │   ├── Project.py
│   │   ├── Skill.py
│   │   ├── Achievement.py
│   │   ├── Education.py
│   │   └── ContactMessage.py
│   ├── routes/              # API route handlers
│   │   ├── personal.py
│   │   ├── experience.py
│   │   ├── projects.py
│   │   ├── skills.py
│   │   ├── achievements.py
│   │   ├── education.py
│   │   └── contact.py
│   ├── database.py          # MongoDB connection
│   ├── server.py            # FastAPI application
│   ├── seed_database.py     # Database seeding script
│   └── requirements.txt
├── contracts.md             # API contracts documentation
├── test_result.md          # Testing documentation
└── README.md               # This file
```

## 🗺 Roadmap

### Phase 1: Core Enhancements ✅
- [x] Full-stack architecture implementation
- [x] Dynamic content management
- [x] Contact form functionality
- [x] Responsive design
- [x] API documentation

### Phase 2: Advanced Features
- [ ] **Admin Dashboard**: Web-based admin panel for content management
- [ ] **Authentication**: JWT-based authentication for admin features
- [ ] **Image Upload**: File upload functionality for project images
- [ ] **Analytics**: Visitor tracking and portfolio analytics
- [ ] **Blog Section**: Dynamic blog with markdown support

### Phase 3: Performance & SEO
- [ ] **SSG/SSR**: Server-side generation for better SEO
- [ ] **CDN Integration**: Image optimization and content delivery
- [ ] **Performance Optimization**: Code splitting and lazy loading
- [ ] **SEO Enhancement**: Meta tags, schema markup, and sitemap

### Phase 4: Advanced Integrations
- [ ] **CI/CD Pipeline**: Automated testing and deployment
- [ ] **Email Notifications**: Automated email responses for contact form
- [ ] **Social Media Integration**: Dynamic social media feeds
- [ ] **Multi-language Support**: Internationalization (i18n)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Guidelines

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Make your changes** following the existing code style
4. **Test your changes** thoroughly
5. **Commit your changes**: `git commit -m 'Add some AmazingFeature'`
6. **Push to the branch**: `git push origin feature/AmazingFeature`
7. **Open a Pull Request**

### Code Standards
- Follow existing code formatting and naming conventions
- Add comments for complex logic
- Ensure all tests pass before submitting
- Update documentation for new features

### Reporting Bugs
- Use the GitHub Issues tab to report bugs
- Include steps to reproduce the issue
- Provide screenshots if applicable
- Specify your environment details

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Shreya Padaganur**
- Email: shreyamp1999@gmail.com
- LinkedIn: [linkedin.com/in/shreyamp](https://www.linkedin.com/in/shreyamp/)
- GitHub: [github.com/ShreyaMP1999](https://github.com/ShreyaMP1999)
- Portfolio: [Your Portfolio URL]

---

## 🙏 Acknowledgments

- [shadcn/ui](https://ui.shadcn.com/) for the beautiful component library
- [Lucide](https://lucide.dev/) for the amazing icon set
- [Tailwind CSS](https://tailwindcss.com/) for the utility-first CSS framework
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent Python web framework
- [React](https://reactjs.org/) for the powerful frontend library

---

**⭐ If you found this project helpful, please consider giving it a star!**

Made with ❤️ and lots of ☕ by Shreya Padaganur -->
