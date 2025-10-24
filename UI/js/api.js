// API Client for Backend Communication

class APIClient {
    constructor(baseURL) {
        this.baseURL = baseURL;
    }

    /**
     * Make HTTP request
     */
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const config = {
            method: options.method || 'GET',
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            }
        };

        if (options.body) {
            config.body = JSON.stringify(options.body);
        }

        try {
            const response = await fetch(url, config);

            if (!response.ok) {
                const error = await response.json().catch(() => ({
                    error: `HTTP Error: ${response.status}`
                }));
                throw new Error(error.error || error.message || 'Request failed');
            }

            return await response.json();
        } catch (error) {
            console.error('API Request Error:', error);
            throw error;
        }
    }

    /**
     * GET request
     */
    async get(endpoint, params = {}) {
        const queryString = new URLSearchParams(params).toString();
        const url = queryString ? `${endpoint}?${queryString}` : endpoint;
        return this.request(url, { method: 'GET' });
    }

    /**
     * POST request
     */
    async post(endpoint, data = {}) {
        return this.request(endpoint, {
            method: 'POST',
            body: data
        });
    }

    /**
     * PUT request
     */
    async put(endpoint, data = {}) {
        return this.request(endpoint, {
            method: 'PUT',
            body: data
        });
    }

    /**
     * DELETE request
     */
    async delete(endpoint) {
        return this.request(endpoint, { method: 'DELETE' });
    }
}

// Create API client instance
const api = new APIClient(API_BASE_URL);

// Driving Style API
const drivingAPI = {
    /**
     * Predict driving style
     */
    async predictDrivingStyle(data) {
        return api.post(API_ENDPOINTS.DRIVING_PREDICT, data);
    },

    /**
     * Get demo data
     */
    async getDemoData() {
        return api.get(API_ENDPOINTS.DRIVING_DEMO);
    }
};

// Weather API
const weatherAPI = {
    /**
     * Get weather data (GET)
     */
    async getWeather(lat, lon, units = 'metric') {
        return api.get(API_ENDPOINTS.WEATHER_GET, { lat, lon, units });
    },

    /**
     * Get weather data (POST)
     */
    async getWeatherPost(data) {
        return api.post(API_ENDPOINTS.WEATHER_POST, data);
    }
};

// Battery Range API
const batteryAPI = {
    /**
     * Predict battery range
     */
    async predictRange(data) {
        return api.post(API_ENDPOINTS.BATTERY_PREDICT, data);
    }
};

// Optimal Path API
const optimalPathAPI = {
    /**
     * Predict optimal path with travel time
     */
    async predictPath(data) {
        return api.post(API_ENDPOINTS.OPTIMAL_PATH_PREDICT, data);
    }
};

// Energy API
const energyAPI = {
    /**
     * Predict energy consumption
     */
    async predictConsumption(data) {
        return api.post(API_ENDPOINTS.ENERGY_PREDICT, data);
    }
};