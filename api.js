import axios from "axios";

const API_BASE = "http://127.0.0.1:8000"; // Your FastAPI backend URL

// Generic CRUD API
export const getMaster = (type) => axios.get(`${API_BASE}/${type}/`);
export const createMaster = (type, data) => axios.post(`${API_BASE}/${type}/`, data);
export const deleteMaster = (type, code) => axios.delete(`${API_BASE}/${type}/${code}`);
