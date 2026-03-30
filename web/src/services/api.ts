import axios from "axios";

/**
 * Pre-configured Axios instance for API calls.
 * Base URL is "/api" which Vite proxies to the FastAPI backend.
 */
const api = axios.create({
  baseURL: "/api",
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
