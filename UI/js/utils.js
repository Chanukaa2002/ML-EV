// Utility Functions

/**
 * Show loading spinner
 */
function showLoading(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = `
            <div class="loading-spinner">
                <div class="spinner"></div>
                <p>Loading...</p>
            </div>
        `;
    }
}

/**
 * Hide loading spinner
 */
function hideLoading(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = '';
    }
}

/**
 * Show error message
 */
function showError(message, elementId = 'error-container') {
    const container = document.getElementById(elementId);
    if (container) {
        container.innerHTML = `
            <div class="alert alert-error">
                <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="8" x2="12" y2="12"></line>
                    <line x1="12" y1="16" x2="12.01" y2="16"></line>
                </svg>
                <span>${message}</span>
                <button onclick="this.parentElement.remove()" class="close-btn">&times;</button>
            </div>
        `;
        setTimeout(() => container.innerHTML = '', 5000);
    }
}

/**
 * Show success message
 */
function showSuccess(message, elementId = 'success-container') {
    const container = document.getElementById(elementId);
    if (container) {
        container.innerHTML = `
            <div class="alert alert-success">
                <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                <span>${message}</span>
                <button onclick="this.parentElement.remove()" class="close-btn">&times;</button>
            </div>
        `;
        setTimeout(() => container.innerHTML = '', 5000);
    }
}

/**
 * Format number with decimals
 */
function formatNumber(num, decimals = 2) {
    return Number(num).toFixed(decimals);
}

/**
 * Format distance
 */
function formatDistance(km) {
    return `${formatNumber(km, 1)} km`;
}

/**
 * Format energy
 */
function formatEnergy(kwh) {
    return `${formatNumber(kwh, 2)} kWh`;
}

/**
 * Format percentage
 */
function formatPercentage(value) {
    return `${formatNumber(value, 1)}%`;
}

/**
 * Calculate percentage
 */
function calculatePercentage(value, total) {
    return (value / total) * 100;
}

/**
 * Validate form field
 */
function validateField(value, type = 'text', required = true) {
    if (required && (!value || value.trim() === '')) {
        return { valid: false, error: 'This field is required' };
    }

    if (type === 'number' && isNaN(value)) {
        return { valid: false, error: 'Please enter a valid number' };
    }

    if (type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
        return { valid: false, error: 'Please enter a valid email' };
    }

    return { valid: true };
}

/**
 * Debounce function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Get driving style color
 */
function getDrivingStyleColor(style) {
    const colors = {
        'Eco': CHART_COLORS.eco,
        'Normal': CHART_COLORS.normal,
        'Aggressive': CHART_COLORS.aggressive
    };
    return colors[style] || CHART_COLORS.primary;
}

/**
 * Get driving style badge HTML
 */
function getDrivingStyleBadge(style) {
    const color = getDrivingStyleColor(style);
    return `<span class="badge" style="background-color: ${color}20; color: ${color}; border: 1px solid ${color};">${style}</span>`;
}

/**
 * Create card HTML
 */
function createCard(title, content, footer = '') {
    return `
        <div class="card">
            <div class="card-header">
                <h3>${title}</h3>
            </div>
            <div class="card-body">
                ${content}
            </div>
            ${footer ? `<div class="card-footer">${footer}</div>` : ''}
        </div>
    `;
}

/**
 * Create stat card HTML
 */
function createStatCard(title, value, icon = '', trend = null) {
    return `
        <div class="stat-card">
            <div class="stat-icon">${icon}</div>
            <div class="stat-content">
                <div class="stat-label">${title}</div>
                <div class="stat-value">${value}</div>
                ${trend !== null ? `<div class="stat-trend ${trend >= 0 ? 'positive' : 'negative'}">${trend >= 0 ? '↑' : '↓'} ${Math.abs(trend)}%</div>` : ''}
            </div>
        </div>
    `;
}

/**
 * Populate select dropdown
 */
function populateSelect(selectId, options, valueKey = 'value', textKey = 'text') {
    const select = document.getElementById(selectId);
    if (!select) return;

    select.innerHTML = '<option value="">-- Select --</option>';
    options.forEach(option => {
        const opt = document.createElement('option');
        opt.value = typeof option === 'object' ? option[valueKey] : option;
        opt.textContent = typeof option === 'object' ? option[textKey] : option;
        select.appendChild(opt);
    });
}

/**
 * Get city coordinates
 */
function getCityCoordinates(cityName) {
    const city = SRI_LANKAN_CITIES.find(c => c.name === cityName);
    return city ? { lat: city.lat, lon: city.lon } : null;
}

/**
 * Calculate distance between two points (Haversine formula)
 */
function calculateDistance(lat1, lon1, lat2, lon2) {
    const R = 6371; // Earth's radius in km
    const dLat = toRad(lat2 - lat1);
    const dLon = toRad(lon2 - lon1);
    const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
              Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) *
              Math.sin(dLon / 2) * Math.sin(dLon / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return R * c;
}

function toRad(degrees) {
    return degrees * (Math.PI / 180);
}

/**
 * Format date and time
 */
function formatDateTime(date = new Date()) {
    return date.toLocaleString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

/**
 * Store data in localStorage
 */
function saveToStorage(key, data) {
    try {
        localStorage.setItem(key, JSON.stringify(data));
        return true;
    } catch (error) {
        console.error('Error saving to storage:', error);
        return false;
    }
}

/**
 * Get data from localStorage
 */
function getFromStorage(key) {
    try {
        const data = localStorage.getItem(key);
        return data ? JSON.parse(data) : null;
    } catch (error) {
        console.error('Error reading from storage:', error);
        return null;
    }
}

/**
 * Clear storage
 */
function clearStorage(key = null) {
    if (key) {
        localStorage.removeItem(key);
    } else {
        localStorage.clear();
    }
}