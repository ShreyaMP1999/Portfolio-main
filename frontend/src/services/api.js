import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for logging
apiClient.interceptors.request.use(
  (config) => {
    console.log(`Making ${config.method?.toUpperCase()} request to ${config.url}`);
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

// Personal Information API
export const personalInfoApi = {
  get: async () => {
    const response = await apiClient.get('/personal/');
    return response.data;
  },
  update: async (data) => {
    const response = await apiClient.put('/personal/', data);
    return response.data;
  },
};

// Experience API
export const experienceApi = {
  getAll: async () => {
    const response = await apiClient.get('/experience/');
    return response.data;
  },
  create: async (data) => {
    const response = await apiClient.post('/experience/', data);
    return response.data;
  },
  update: async (id, data) => {
    const response = await apiClient.put(`/experience/${id}`, data);
    return response.data;
  },
  delete: async (id) => {
    const response = await apiClient.delete(`/experience/${id}`);
    return response.data;
  },
};

// Projects API
export const projectsApi = {
  getAll: async () => {
    const response = await apiClient.get('/projects/');
    return response.data;
  },
  getByCategory: async (category) => {
    const response = await apiClient.get(`/projects/category/${encodeURIComponent(category)}`);
    return response.data;
  },
  create: async (data) => {
    const response = await apiClient.post('/projects/', data);
    return response.data;
  },
  update: async (id, data) => {
    const response = await apiClient.put(`/projects/${id}`, data);
    return response.data;
  },
  delete: async (id) => {
    const response = await apiClient.delete(`/projects/${id}`);
    return response.data;
  },
};

// Skills API
export const skillsApi = {
  getAll: async () => {
    const response = await apiClient.get('/skills/');
    return response.data;
  },
  create: async (data) => {
    const response = await apiClient.post('/skills/', data);
    return response.data;
  },
  update: async (id, data) => {
    const response = await apiClient.put(`/skills/${id}`, data);
    return response.data;
  },
  delete: async (id) => {
    const response = await apiClient.delete(`/skills/${id}`);
    return response.data;
  },
};

// Achievements API
export const achievementsApi = {
  getAll: async () => {
    const response = await apiClient.get('/achievements/');
    return response.data;
  },
  create: async (data) => {
    const response = await apiClient.post('/achievements/', data);
    return response.data;
  },
  update: async (id, data) => {
    const response = await apiClient.put(`/achievements/${id}`, data);
    return response.data;
  },
  delete: async (id) => {
    const response = await apiClient.delete(`/achievements/${id}`);
    return response.data;
  },
};

// Education API
export const educationApi = {
  getAll: async () => {
    const response = await apiClient.get('/education/');
    return response.data;
  },
  create: async (data) => {
    const response = await apiClient.post('/education/', data);
    return response.data;
  },
  update: async (id, data) => {
    const response = await apiClient.put(`/education/${id}`, data);
    return response.data;
  },
  delete: async (id) => {
    const response = await apiClient.delete(`/education/${id}`);
    return response.data;
  },
};

// Contact API
export const contactApi = {
  submit: async (data) => {
    const response = await apiClient.post('/contact/', data);
    return response.data;
  },
  getMessages: async () => {
    const response = await apiClient.get('/contact/messages');
    return response.data;
  },
  markAsRead: async (id) => {
    const response = await apiClient.put(`/contact/messages/${id}/read`);
    return response.data;
  },
};

// Helper function to handle API errors
export const handleApiError = (error, fallbackMessage = 'An error occurred') => {
  if (error.response?.data?.detail) {
    return error.response.data.detail;
  }
  if (error.response?.data?.message) {
    return error.response.data.message;
  }
  if (error.message) {
    return error.message;
  }
  return fallbackMessage;
};

export default apiClient;