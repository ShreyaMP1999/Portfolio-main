# Portfolio Backend Integration Contracts

## Overview
Transform the frontend-only portfolio with mock data into a full-stack application with MongoDB backend, allowing dynamic content management and real-time updates.

## Current Mock Data Structure (mock.js)
- **personalInfo**: Basic profile information
- **experience**: Professional experience entries
- **education**: Educational background
- **projects**: Project portfolio with details
- **skills**: Categorized technical skills
- **achievements**: Awards and leadership roles
- **socialLinks**: Social media profiles

## Backend Implementation Plan

### 1. Database Models (MongoDB)

#### PersonalInfo Collection
```
{
  _id: ObjectId,
  name: String,
  title: String,
  location: String,
  email: String,
  phone: String,
  linkedin: String,
  github: String,
  bio: String,
  tagline: String,
  isActive: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

#### Experience Collection
```
{
  _id: ObjectId,
  company: String,
  position: String,
  duration: String,
  location: String,
  type: String,
  responsibilities: [String],
  technologies: [String],
  order: Number,
  isActive: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

#### Projects Collection
```
{
  _id: ObjectId,
  title: String,
  description: String,
  longDescription: String,
  technologies: [String],
  features: [String],
  github: String,
  demo: String,
  image: String,
  category: String,
  order: Number,
  isActive: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

#### Skills Collection
```
{
  _id: ObjectId,
  category: String,
  skills: [String],
  order: Number,
  isActive: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

#### Achievements Collection
```
{
  _id: ObjectId,
  title: String,
  organization: String,
  year: String,
  description: String,
  order: Number,
  isActive: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

#### ContactMessages Collection
```
{
  _id: ObjectId,
  name: String,
  email: String,
  subject: String,
  message: String,
  isRead: Boolean,
  createdAt: Date
}
```

### 2. API Endpoints

#### Personal Information
- `GET /api/personal` - Get personal information
- `PUT /api/personal` - Update personal information

#### Experience
- `GET /api/experience` - Get all experience entries
- `POST /api/experience` - Create new experience entry
- `PUT /api/experience/:id` - Update experience entry
- `DELETE /api/experience/:id` - Delete experience entry

#### Projects
- `GET /api/projects` - Get all projects
- `GET /api/projects/:category` - Get projects by category
- `POST /api/projects` - Create new project
- `PUT /api/projects/:id` - Update project
- `DELETE /api/projects/:id` - Delete project

#### Skills
- `GET /api/skills` - Get all skills by categories
- `POST /api/skills` - Create new skill category
- `PUT /api/skills/:id` - Update skill category
- `DELETE /api/skills/:id` - Delete skill category

#### Achievements
- `GET /api/achievements` - Get all achievements
- `POST /api/achievements` - Create new achievement
- `PUT /api/achievements/:id` - Update achievement
- `DELETE /api/achievements/:id` - Delete achievement

#### Contact
- `POST /api/contact` - Submit contact form
- `GET /api/contact/messages` - Get all contact messages (admin)

#### Education
- `GET /api/education` - Get education information
- `POST /api/education` - Create education entry
- `PUT /api/education/:id` - Update education entry
- `DELETE /api/education/:id` - Delete education entry

### 3. Frontend Integration Changes

#### Data Fetching Service
Create `src/services/api.js` with:
- API client configuration using REACT_APP_BACKEND_URL
- Service functions for each endpoint
- Error handling and loading states

#### Component Updates
- Replace mock data imports with API calls
- Add loading states and error handling
- Implement real contact form submission
- Add admin capabilities for content management

#### State Management
- Add React Context for global state management
- Implement caching for frequently accessed data
- Handle real-time updates and optimistic updates

### 4. Backend Implementation Steps

1. **Database Setup**: Initialize collections with current mock data
2. **Models Creation**: Mongoose schemas for each collection
3. **API Routes**: RESTful endpoints with proper validation
4. **Error Handling**: Comprehensive error handling and logging
5. **Data Migration**: Seed database with current mock data
6. **Testing**: API endpoint testing

### 5. Frontend Integration Steps

1. **API Service Layer**: Create centralized API communication
2. **Component Refactoring**: Replace mock data with API calls
3. **Loading States**: Add loading indicators and error handling
4. **Contact Form**: Implement real form submission
5. **Admin Features**: Basic content management capabilities

### 6. Additional Features to Implement

#### Admin Panel (Optional Enhancement)
- Password-protected admin routes
- CRUD operations for all content
- Contact message management
- Analytics and visitor tracking

#### Performance Optimizations
- API response caching
- Image optimization and CDN integration
- Lazy loading for large datasets
- SEO optimization with meta tags

### 7. Deployment Considerations
- Environment variables for production
- Database indexing for performance
- API rate limiting
- CORS configuration
- SSL/HTTPS setup

## Success Criteria
- All mock data successfully migrated to database
- Frontend seamlessly integrates with backend APIs
- Contact form functional with database storage
- Admin capabilities for content updates
- Responsive design maintained
- Performance optimized for production use

## Timeline
- Phase 1: Backend models and basic CRUD APIs
- Phase 2: Frontend integration and testing
- Phase 3: Enhanced features and optimizations