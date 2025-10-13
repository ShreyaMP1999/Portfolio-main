#!/usr/bin/env python3
"""
Comprehensive Backend API Testing for Portfolio Website
Tests all API endpoints according to the test_result.md requirements
"""

import requests
import json
import sys
from datetime import datetime
import uuid

# Backend URL from frontend/.env
BASE_URL = "https://portfolio-hub-374.preview.emergentagent.com/api"

class PortfolioAPITester:
    def __init__(self):
        self.base_url = BASE_URL
        self.test_results = {
            "passed": 0,
            "failed": 0,
            "errors": []
        }
        self.created_ids = {
            "experience": [],
            "projects": [],
            "skills": [],
            "achievements": [],
            "education": [],
            "contact": []
        }
    
    def log_result(self, test_name, success, message="", response=None):
        """Log test result"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status}: {test_name}")
        if message:
            print(f"   {message}")
        if response and not success:
            print(f"   Response: {response.status_code} - {response.text[:200]}")
        
        if success:
            self.test_results["passed"] += 1
        else:
            self.test_results["failed"] += 1
            self.test_results["errors"].append(f"{test_name}: {message}")
        print()
    
    def test_server_health(self):
        """Test server health endpoints"""
        print("=== Testing Server Health ===")
        
        # Test root API endpoint
        try:
            response = requests.get(f"{self.base_url}/")
            if response.status_code == 200:
                data = response.json()
                if "message" in data and "version" in data:
                    self.log_result("Root API Endpoint", True, f"Message: {data['message']}")
                else:
                    self.log_result("Root API Endpoint", False, "Missing required fields in response")
            else:
                self.log_result("Root API Endpoint", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("Root API Endpoint", False, f"Exception: {str(e)}")
        
        # Test health check endpoint
        try:
            response = requests.get(f"{self.base_url.replace('/api', '')}/health")
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "healthy":
                    self.log_result("Health Check Endpoint", True, f"Status: {data['status']}")
                else:
                    self.log_result("Health Check Endpoint", False, "Service not healthy")
            else:
                self.log_result("Health Check Endpoint", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("Health Check Endpoint", False, f"Exception: {str(e)}")
    
    def test_personal_info_api(self):
        """Test Personal Information API endpoints"""
        print("=== Testing Personal Information API ===")
        
        # Test GET personal info
        try:
            response = requests.get(f"{self.base_url}/personal/")
            if response.status_code == 200:
                data = response.json()
                required_fields = ["name", "title", "email", "bio", "tagline"]
                if all(field in data for field in required_fields):
                    self.log_result("GET Personal Info", True, f"Retrieved info for: {data.get('name', 'Unknown')}")
                else:
                    missing = [f for f in required_fields if f not in data]
                    self.log_result("GET Personal Info", False, f"Missing fields: {missing}")
            else:
                self.log_result("GET Personal Info", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("GET Personal Info", False, f"Exception: {str(e)}")
        
        # Test PUT personal info update
        try:
            update_data = {
                "tagline": "Updated tagline for testing purposes"
            }
            response = requests.put(f"{self.base_url}/personal/", json=update_data)
            if response.status_code == 200:
                data = response.json()
                if data.get("tagline") == update_data["tagline"]:
                    self.log_result("PUT Personal Info Update", True, "Successfully updated tagline")
                else:
                    self.log_result("PUT Personal Info Update", False, "Update not reflected in response")
            else:
                self.log_result("PUT Personal Info Update", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("PUT Personal Info Update", False, f"Exception: {str(e)}")
    
    def test_experience_api(self):
        """Test Experience API endpoints"""
        print("=== Testing Experience API ===")
        
        # Test GET all experiences
        try:
            response = requests.get(f"{self.base_url}/experience/")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    self.log_result("GET All Experiences", True, f"Retrieved {len(data)} experiences")
                    # Store existing experience ID for update/delete tests
                    if data:
                        self.existing_experience_id = data[0]["id"]
                else:
                    self.log_result("GET All Experiences", False, "Response is not a list")
            else:
                self.log_result("GET All Experiences", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("GET All Experiences", False, f"Exception: {str(e)}")
        
        # Test POST new experience
        try:
            new_experience = {
                "company": "Test Company Ltd",
                "position": "Senior Software Engineer",
                "duration": "Jan 2024 - Present",
                "location": "San Francisco, CA",
                "type": "Full-time",
                "responsibilities": [
                    "Led development of microservices architecture",
                    "Mentored junior developers"
                ],
                "technologies": ["Python", "FastAPI", "MongoDB"],
                "order": 999
            }
            response = requests.post(f"{self.base_url}/experience/", json=new_experience)
            if response.status_code == 200:
                data = response.json()
                if data.get("company") == new_experience["company"]:
                    self.created_ids["experience"].append(data["id"])
                    self.log_result("POST New Experience", True, f"Created experience: {data['company']}")
                else:
                    self.log_result("POST New Experience", False, "Created data doesn't match input")
            else:
                self.log_result("POST New Experience", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("POST New Experience", False, f"Exception: {str(e)}")
        
        # Test PUT update experience (if we have a created ID)
        if self.created_ids["experience"]:
            try:
                exp_id = self.created_ids["experience"][0]
                update_data = {
                    "position": "Lead Software Engineer"
                }
                response = requests.put(f"{self.base_url}/experience/{exp_id}", json=update_data)
                if response.status_code == 200:
                    data = response.json()
                    if data.get("position") == update_data["position"]:
                        self.log_result("PUT Update Experience", True, "Successfully updated position")
                    else:
                        self.log_result("PUT Update Experience", False, "Update not reflected")
                else:
                    self.log_result("PUT Update Experience", False, f"Status: {response.status_code}", response)
            except Exception as e:
                self.log_result("PUT Update Experience", False, f"Exception: {str(e)}")
        
        # Test DELETE experience (soft delete)
        if self.created_ids["experience"]:
            try:
                exp_id = self.created_ids["experience"][0]
                response = requests.delete(f"{self.base_url}/experience/{exp_id}")
                if response.status_code == 200:
                    data = response.json()
                    if "message" in data:
                        self.log_result("DELETE Experience", True, "Successfully deleted experience")
                    else:
                        self.log_result("DELETE Experience", False, "No confirmation message")
                else:
                    self.log_result("DELETE Experience", False, f"Status: {response.status_code}", response)
            except Exception as e:
                self.log_result("DELETE Experience", False, f"Exception: {str(e)}")
    
    def test_projects_api(self):
        """Test Projects API endpoints"""
        print("=== Testing Projects API ===")
        
        # Test GET all projects
        try:
            response = requests.get(f"{self.base_url}/projects/")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    self.log_result("GET All Projects", True, f"Retrieved {len(data)} projects")
                else:
                    self.log_result("GET All Projects", False, "Response is not a list")
            else:
                self.log_result("GET All Projects", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("GET All Projects", False, f"Exception: {str(e)}")
        
        # Test GET projects by category
        try:
            response = requests.get(f"{self.base_url}/projects/category/AI/ML")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    self.log_result("GET Projects by Category", True, f"Retrieved {len(data)} AI/ML projects")
                else:
                    self.log_result("GET Projects by Category", False, "Response is not a list")
            else:
                self.log_result("GET Projects by Category", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("GET Projects by Category", False, f"Exception: {str(e)}")
        
        # Test POST new project
        try:
            new_project = {
                "title": "Test Portfolio API",
                "description": "A comprehensive API testing suite",
                "long_description": "This project demonstrates automated testing of portfolio APIs with comprehensive coverage of all endpoints.",
                "technologies": ["Python", "FastAPI", "MongoDB", "Requests"],
                "features": [
                    "Automated endpoint testing",
                    "Comprehensive error handling",
                    "Real-time result reporting"
                ],
                "github": "https://github.com/test/portfolio-api-test",
                "demo": "https://demo.test-portfolio-api.com",
                "image": "https://images.test.com/portfolio-api.jpg",
                "category": "Full Stack",
                "order": 999
            }
            response = requests.post(f"{self.base_url}/projects/", json=new_project)
            if response.status_code == 200:
                data = response.json()
                if data.get("title") == new_project["title"]:
                    self.created_ids["projects"].append(data["id"])
                    self.log_result("POST New Project", True, f"Created project: {data['title']}")
                else:
                    self.log_result("POST New Project", False, "Created data doesn't match input")
            else:
                self.log_result("POST New Project", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("POST New Project", False, f"Exception: {str(e)}")
        
        # Test PUT update project
        if self.created_ids["projects"]:
            try:
                project_id = self.created_ids["projects"][0]
                update_data = {
                    "description": "An enhanced API testing suite with advanced features"
                }
                response = requests.put(f"{self.base_url}/projects/{project_id}", json=update_data)
                if response.status_code == 200:
                    data = response.json()
                    if data.get("description") == update_data["description"]:
                        self.log_result("PUT Update Project", True, "Successfully updated description")
                    else:
                        self.log_result("PUT Update Project", False, "Update not reflected")
                else:
                    self.log_result("PUT Update Project", False, f"Status: {response.status_code}", response)
            except Exception as e:
                self.log_result("PUT Update Project", False, f"Exception: {str(e)}")
        
        # Test DELETE project
        if self.created_ids["projects"]:
            try:
                project_id = self.created_ids["projects"][0]
                response = requests.delete(f"{self.base_url}/projects/{project_id}")
                if response.status_code == 200:
                    data = response.json()
                    if "message" in data:
                        self.log_result("DELETE Project", True, "Successfully deleted project")
                    else:
                        self.log_result("DELETE Project", False, "No confirmation message")
                else:
                    self.log_result("DELETE Project", False, f"Status: {response.status_code}", response)
            except Exception as e:
                self.log_result("DELETE Project", False, f"Exception: {str(e)}")
    
    def test_skills_api(self):
        """Test Skills API endpoints"""
        print("=== Testing Skills API ===")
        
        # Test GET all skills
        try:
            response = requests.get(f"{self.base_url}/skills/")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    self.log_result("GET All Skills", True, f"Retrieved {len(data)} skill categories")
                else:
                    self.log_result("GET All Skills", False, "Response is not a list")
            else:
                self.log_result("GET All Skills", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("GET All Skills", False, f"Exception: {str(e)}")
        
        # Test POST new skill category
        try:
            new_skill = {
                "category": "Testing & QA",
                "skills": ["Unit Testing", "Integration Testing", "API Testing", "Automated Testing"],
                "order": 999
            }
            response = requests.post(f"{self.base_url}/skills/", json=new_skill)
            if response.status_code == 200:
                data = response.json()
                if data.get("category") == new_skill["category"]:
                    self.created_ids["skills"].append(data["id"])
                    self.log_result("POST New Skill Category", True, f"Created category: {data['category']}")
                else:
                    self.log_result("POST New Skill Category", False, "Created data doesn't match input")
            else:
                self.log_result("POST New Skill Category", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("POST New Skill Category", False, f"Exception: {str(e)}")
        
        # Test PUT update skills
        if self.created_ids["skills"]:
            try:
                skill_id = self.created_ids["skills"][0]
                update_data = {
                    "skills": ["Unit Testing", "Integration Testing", "API Testing", "Automated Testing", "Performance Testing"]
                }
                response = requests.put(f"{self.base_url}/skills/{skill_id}", json=update_data)
                if response.status_code == 200:
                    data = response.json()
                    if len(data.get("skills", [])) == len(update_data["skills"]):
                        self.log_result("PUT Update Skills", True, "Successfully updated skills list")
                    else:
                        self.log_result("PUT Update Skills", False, "Update not reflected properly")
                else:
                    self.log_result("PUT Update Skills", False, f"Status: {response.status_code}", response)
            except Exception as e:
                self.log_result("PUT Update Skills", False, f"Exception: {str(e)}")
        
        # Test DELETE skill category
        if self.created_ids["skills"]:
            try:
                skill_id = self.created_ids["skills"][0]
                response = requests.delete(f"{self.base_url}/skills/{skill_id}")
                if response.status_code == 200:
                    data = response.json()
                    if "message" in data:
                        self.log_result("DELETE Skill Category", True, "Successfully deleted skill category")
                    else:
                        self.log_result("DELETE Skill Category", False, "No confirmation message")
                else:
                    self.log_result("DELETE Skill Category", False, f"Status: {response.status_code}", response)
            except Exception as e:
                self.log_result("DELETE Skill Category", False, f"Exception: {str(e)}")
    
    def test_achievements_api(self):
        """Test Achievements API endpoints"""
        print("=== Testing Achievements API ===")
        
        # Test GET all achievements
        try:
            response = requests.get(f"{self.base_url}/achievements/")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    self.log_result("GET All Achievements", True, f"Retrieved {len(data)} achievements")
                else:
                    self.log_result("GET All Achievements", False, "Response is not a list")
            else:
                self.log_result("GET All Achievements", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("GET All Achievements", False, f"Exception: {str(e)}")
        
        # Test POST new achievement
        try:
            new_achievement = {
                "title": "API Testing Excellence Award",
                "organization": "Tech Testing Institute",
                "year": "2024",
                "description": "Recognized for developing comprehensive API testing frameworks and methodologies",
                "order": 999
            }
            response = requests.post(f"{self.base_url}/achievements/", json=new_achievement)
            if response.status_code == 200:
                data = response.json()
                if data.get("title") == new_achievement["title"]:
                    self.created_ids["achievements"].append(data["id"])
                    self.log_result("POST New Achievement", True, f"Created achievement: {data['title']}")
                else:
                    self.log_result("POST New Achievement", False, "Created data doesn't match input")
            else:
                self.log_result("POST New Achievement", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("POST New Achievement", False, f"Exception: {str(e)}")
        
        # Test PUT update achievement
        if self.created_ids["achievements"]:
            try:
                achievement_id = self.created_ids["achievements"][0]
                update_data = {
                    "description": "Recognized for developing comprehensive API testing frameworks, methodologies, and best practices"
                }
                response = requests.put(f"{self.base_url}/achievements/{achievement_id}", json=update_data)
                if response.status_code == 200:
                    data = response.json()
                    if data.get("description") == update_data["description"]:
                        self.log_result("PUT Update Achievement", True, "Successfully updated description")
                    else:
                        self.log_result("PUT Update Achievement", False, "Update not reflected")
                else:
                    self.log_result("PUT Update Achievement", False, f"Status: {response.status_code}", response)
            except Exception as e:
                self.log_result("PUT Update Achievement", False, f"Exception: {str(e)}")
        
        # Test DELETE achievement
        if self.created_ids["achievements"]:
            try:
                achievement_id = self.created_ids["achievements"][0]
                response = requests.delete(f"{self.base_url}/achievements/{achievement_id}")
                if response.status_code == 200:
                    data = response.json()
                    if "message" in data:
                        self.log_result("DELETE Achievement", True, "Successfully deleted achievement")
                    else:
                        self.log_result("DELETE Achievement", False, "No confirmation message")
                else:
                    self.log_result("DELETE Achievement", False, f"Status: {response.status_code}", response)
            except Exception as e:
                self.log_result("DELETE Achievement", False, f"Exception: {str(e)}")
    
    def test_education_api(self):
        """Test Education API endpoints"""
        print("=== Testing Education API ===")
        
        # Test GET all education
        try:
            response = requests.get(f"{self.base_url}/education/")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    self.log_result("GET All Education", True, f"Retrieved {len(data)} education entries")
                else:
                    self.log_result("GET All Education", False, "Response is not a list")
            else:
                self.log_result("GET All Education", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("GET All Education", False, f"Exception: {str(e)}")
        
        # Test POST new education
        try:
            new_education = {
                "degree": "Certificate in API Testing",
                "school": "Tech Education Institute",
                "location": "Online",
                "duration": "2024",
                "gpa": "4.0",
                "relevant_courses": ["API Design", "Testing Methodologies", "Automation Frameworks"],
                "achievements": ["Top 5% of class", "Perfect attendance"],
                "order": 999
            }
            response = requests.post(f"{self.base_url}/education/", json=new_education)
            if response.status_code == 200:
                data = response.json()
                if data.get("degree") == new_education["degree"]:
                    self.created_ids["education"].append(data["id"])
                    self.log_result("POST New Education", True, f"Created education: {data['degree']}")
                else:
                    self.log_result("POST New Education", False, "Created data doesn't match input")
            else:
                self.log_result("POST New Education", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("POST New Education", False, f"Exception: {str(e)}")
        
        # Test PUT update education
        if self.created_ids["education"]:
            try:
                education_id = self.created_ids["education"][0]
                update_data = {
                    "achievements": ["Top 5% of class", "Perfect attendance", "Outstanding project award"]
                }
                response = requests.put(f"{self.base_url}/education/{education_id}", json=update_data)
                if response.status_code == 200:
                    data = response.json()
                    if len(data.get("achievements", [])) == len(update_data["achievements"]):
                        self.log_result("PUT Update Education", True, "Successfully updated achievements")
                    else:
                        self.log_result("PUT Update Education", False, "Update not reflected properly")
                else:
                    self.log_result("PUT Update Education", False, f"Status: {response.status_code}", response)
            except Exception as e:
                self.log_result("PUT Update Education", False, f"Exception: {str(e)}")
        
        # Test DELETE education
        if self.created_ids["education"]:
            try:
                education_id = self.created_ids["education"][0]
                response = requests.delete(f"{self.base_url}/education/{education_id}")
                if response.status_code == 200:
                    data = response.json()
                    if "message" in data:
                        self.log_result("DELETE Education", True, "Successfully deleted education entry")
                    else:
                        self.log_result("DELETE Education", False, "No confirmation message")
                else:
                    self.log_result("DELETE Education", False, f"Status: {response.status_code}", response)
            except Exception as e:
                self.log_result("DELETE Education", False, f"Exception: {str(e)}")
    
    def test_contact_api(self):
        """Test Contact API endpoints"""
        print("=== Testing Contact API ===")
        
        # Test POST contact form submission
        try:
            contact_message = {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "subject": "API Testing Inquiry",
                "message": "I'm interested in learning more about your API testing capabilities and methodologies. Could we schedule a discussion?"
            }
            response = requests.post(f"{self.base_url}/contact/", json=contact_message)
            if response.status_code == 200:
                data = response.json()
                if data.get("name") == contact_message["name"]:
                    self.created_ids["contact"].append(data["id"])
                    self.log_result("POST Contact Form", True, f"Submitted message from: {data['name']}")
                else:
                    self.log_result("POST Contact Form", False, "Submitted data doesn't match input")
            else:
                self.log_result("POST Contact Form", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("POST Contact Form", False, f"Exception: {str(e)}")
        
        # Test GET all contact messages (admin)
        try:
            response = requests.get(f"{self.base_url}/contact/messages")
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    self.log_result("GET All Contact Messages", True, f"Retrieved {len(data)} messages")
                else:
                    self.log_result("GET All Contact Messages", False, "Response is not a list")
            else:
                self.log_result("GET All Contact Messages", False, f"Status: {response.status_code}", response)
        except Exception as e:
            self.log_result("GET All Contact Messages", False, f"Exception: {str(e)}")
        
        # Test PUT mark message as read
        if self.created_ids["contact"]:
            try:
                message_id = self.created_ids["contact"][0]
                response = requests.put(f"{self.base_url}/contact/messages/{message_id}/read")
                if response.status_code == 200:
                    data = response.json()
                    if "message" in data:
                        self.log_result("PUT Mark Message as Read", True, "Successfully marked message as read")
                    else:
                        self.log_result("PUT Mark Message as Read", False, "No confirmation message")
                else:
                    self.log_result("PUT Mark Message as Read", False, f"Status: {response.status_code}", response)
            except Exception as e:
                self.log_result("PUT Mark Message as Read", False, f"Exception: {str(e)}")
    
    def test_error_handling(self):
        """Test error handling for invalid requests"""
        print("=== Testing Error Handling ===")
        
        # Test 404 for non-existent resource
        try:
            fake_id = str(uuid.uuid4())
            response = requests.get(f"{self.base_url}/experience/{fake_id}")
            if response.status_code == 404:
                self.log_result("404 Error Handling", True, "Correctly returned 404 for non-existent resource")
            else:
                self.log_result("404 Error Handling", False, f"Expected 404, got {response.status_code}")
        except Exception as e:
            self.log_result("404 Error Handling", False, f"Exception: {str(e)}")
        
        # Test validation error for invalid data
        try:
            invalid_experience = {
                "company": "",  # Empty required field
                "position": "Test Position"
                # Missing other required fields
            }
            response = requests.post(f"{self.base_url}/experience/", json=invalid_experience)
            if response.status_code in [400, 422]:  # Bad Request or Unprocessable Entity
                self.log_result("Validation Error Handling", True, f"Correctly returned {response.status_code} for invalid data")
            else:
                self.log_result("Validation Error Handling", False, f"Expected 400/422, got {response.status_code}")
        except Exception as e:
            self.log_result("Validation Error Handling", False, f"Exception: {str(e)}")
    
    def run_all_tests(self):
        """Run all API tests"""
        print(f"🚀 Starting Portfolio API Testing")
        print(f"📍 Base URL: {self.base_url}")
        print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        # Run all test suites
        self.test_server_health()
        self.test_personal_info_api()
        self.test_experience_api()
        self.test_projects_api()
        self.test_skills_api()
        self.test_achievements_api()
        self.test_education_api()
        self.test_contact_api()
        self.test_error_handling()
        
        # Print final results
        print("=" * 60)
        print("🏁 FINAL TEST RESULTS")
        print("=" * 60)
        print(f"✅ Passed: {self.test_results['passed']}")
        print(f"❌ Failed: {self.test_results['failed']}")
        print(f"📊 Success Rate: {(self.test_results['passed'] / (self.test_results['passed'] + self.test_results['failed']) * 100):.1f}%")
        
        if self.test_results['errors']:
            print("\n🚨 FAILED TESTS:")
            for error in self.test_results['errors']:
                print(f"   • {error}")
        
        print(f"\n⏰ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        return self.test_results['failed'] == 0

if __name__ == "__main__":
    tester = PortfolioAPITester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)