# 🚀 EV Route Optimizer - Deployment Guide

## 📋 Table of Contents
- [Development Setup](#development-setup)
- [Production Build](#production-build)
- [Deployment Options](#deployment-options)
- [Environment Configuration](#environment-configuration)
- [Troubleshooting](#troubleshooting)

---

## 🛠️ Development Setup

### Prerequisites Check
```powershell
# Check Node.js (required: v18+)
node --version

# Check npm
npm --version

# Check Python (required: 3.8+)
python --version

# Check pip
pip --version
```

### Quick Setup
```powershell
# Clone and navigate
git clone https://github.com/Chanukaa2002/ML-EV.git
cd ML-EV

# Run automated setup
.\setup.ps1

# Start both servers
.\start-all.ps1
```

### Manual Setup

#### Backend
```powershell
cd backend
pip install -r requirements.txt
python app.py
```

#### Frontend
```powershell
cd frontend
npm install
npm run dev
```

---

## 🏗️ Production Build

### Build Frontend for Production

```powershell
cd frontend
npm run build
```

This creates an optimized production build in `frontend/dist/` folder.

### Preview Production Build

```powershell
npm run preview
```

---

## 🌐 Deployment Options

### Option 1: Vercel (Frontend) + Render/Railway (Backend)

#### Frontend on Vercel

1. **Install Vercel CLI**
   ```powershell
   npm install -g vercel
   ```

2. **Deploy**
   ```powershell
   cd frontend
   vercel
   ```

3. **Configure Environment**
   - Add `VITE_API_BASE_URL` in Vercel dashboard
   - Point to your backend URL

#### Backend on Render

1. Create account on [Render](https://render.com)
2. Create new **Web Service**
3. Connect GitHub repository
4. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Environment:** Python 3
5. Add environment variables:
   - `PORT`: 5000
   - `OPENWEATHER_API_KEY`: your_api_key

### Option 2: Traditional VPS (DigitalOcean, AWS, etc.)

#### Server Requirements
- Ubuntu 20.04+ or similar
- 2GB RAM minimum
- Node.js 18+
- Python 3.8+
- Nginx (for reverse proxy)

#### Backend Setup on VPS

```bash
# Install Python dependencies
sudo apt update
sudo apt install python3-pip python3-venv

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Run with Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Frontend Build & Deploy

```bash
# Build locally
npm run build

# Upload dist folder to VPS
scp -r dist/* user@your-server:/var/www/ev-optimizer

# Configure Nginx
sudo nano /etc/nginx/sites-available/ev-optimizer
```

**Nginx Configuration:**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    # Frontend
    location / {
        root /var/www/ev-optimizer;
        try_files $uri $uri/ /index.html;
    }

    # Backend API
    location /api {
        proxy_pass http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/ev-optimizer /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Option 3: Docker Deployment

#### Backend Dockerfile

Create `backend/Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

#### Frontend Dockerfile

Create `frontend/Dockerfile`:
```dockerfile
FROM node:18-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

#### Docker Compose

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - PORT=5000
    restart: unless-stopped

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
    environment:
      - VITE_API_BASE_URL=http://backend:5000/api
    restart: unless-stopped
```

**Deploy with Docker:**
```powershell
docker-compose up -d
```

---

## ⚙️ Environment Configuration

### Development (.env)
```env
# Frontend
VITE_API_BASE_URL=http://localhost:5000/api

# Backend
FLASK_ENV=development
FLASK_DEBUG=1
HOST=0.0.0.0
PORT=5000
OPENWEATHER_API_KEY=your_api_key_here
```

### Production (.env)
```env
# Frontend
VITE_API_BASE_URL=https://api.your-domain.com/api

# Backend
FLASK_ENV=production
FLASK_DEBUG=0
HOST=0.0.0.0
PORT=5000
OPENWEATHER_API_KEY=your_api_key_here
```

---

## 🔒 Security Considerations

### Backend
1. **Move API key to environment variable**
   ```python
   # In external_api_controller.py
   api_key = os.getenv("OPENWEATHER_API_KEY")
   ```

2. **Enable HTTPS**
   - Use Let's Encrypt for free SSL
   - Configure Nginx with SSL

3. **CORS Configuration**
   ```python
   # In app.py - restrict origins in production
   CORS(app, resources={r"/api/*": {
       "origins": ["https://your-domain.com"]
   }})
   ```

4. **Rate Limiting**
   ```python
   from flask_limiter import Limiter
   
   limiter = Limiter(
       app,
       key_func=lambda: request.remote_addr
   )
   
   @app.route('/api/driving/predict')
   @limiter.limit("100 per hour")
   def predict():
       # ...
   ```

### Frontend
1. **Environment Variables**
   - Never commit `.env` files
   - Use platform-specific env var management

2. **API Keys**
   - Backend should handle sensitive keys
   - Frontend should never expose secrets

---

## 🔍 Health Checks

Add health check endpoint (already exists):

```python
@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    })
```

Test:
```powershell
curl http://localhost:5000/health
```

---

## 📊 Monitoring

### Backend Logging
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

@app.route('/api/driving/predict')
def predict():
    logging.info(f"Prediction request from {request.remote_addr}")
    # ...
```

### Frontend Error Tracking

Consider adding:
- Sentry for error tracking
- Google Analytics for usage
- LogRocket for session replay

---

## 🚦 Performance Optimization

### Frontend
- ✅ Code splitting (React Router handles this)
- ✅ Lazy loading images
- ✅ Minification (Vite handles this)
- Consider: CDN for static assets

### Backend
- Add caching for weather API
  ```python
  from flask_caching import Cache
  
  cache = Cache(app, config={
      'CACHE_TYPE': 'simple',
      'CACHE_DEFAULT_TIMEOUT': 300
  })
  
  @cache.cached(timeout=300)
  def get_weather(lat, lon):
      # ...
  ```

- Use Gunicorn with multiple workers
  ```bash
  gunicorn -w 4 -b 0.0.0.0:5000 app:app
  ```

---

## 🐛 Troubleshooting

### Build Fails
```powershell
# Clear node_modules and reinstall
Remove-Item -Recurse -Force node_modules
npm install

# Clear build cache
npm run build -- --force
```

### API Connection Issues
1. Check CORS settings
2. Verify API URL in .env
3. Check network/firewall
4. Test backend directly: `curl http://localhost:5000/health`

### Module Import Errors
```powershell
# Backend
pip install -r requirements.txt --force-reinstall

# Frontend
npm install --legacy-peer-deps
```

---

## 📝 Deployment Checklist

### Pre-Deployment
- [ ] All features tested locally
- [ ] Environment variables configured
- [ ] API keys secured
- [ ] CORS properly configured
- [ ] Health checks working
- [ ] Error handling implemented
- [ ] Logging configured

### Production Build
- [ ] Frontend builds successfully
- [ ] No console errors
- [ ] All API endpoints work
- [ ] Mobile responsive
- [ ] Browser compatibility tested

### Post-Deployment
- [ ] SSL certificate installed
- [ ] DNS configured
- [ ] Monitoring setup
- [ ] Backup strategy
- [ ] Documentation updated

---

## 🎯 Recommended Stack

**Best for Quick Deploy:**
- Frontend: Vercel (Free tier, automatic HTTPS)
- Backend: Render (Free tier, automatic HTTPS)

**Best for Full Control:**
- VPS: DigitalOcean Droplet ($5/month)
- Domain: Namecheap/GoDaddy
- SSL: Let's Encrypt (Free)

**Best for Scalability:**
- Frontend: AWS S3 + CloudFront
- Backend: AWS Elastic Beanstalk
- Database: AWS RDS (if needed)

---

## 🆘 Support Resources

- [Vite Deployment Guide](https://vitejs.dev/guide/static-deploy.html)
- [Flask Deployment Options](https://flask.palletsprojects.com/en/2.3.x/deploying/)
- [Nginx Configuration](https://www.nginx.com/resources/wiki/start/)
- [Docker Documentation](https://docs.docker.com/)

---

**Ready to deploy!** Choose your deployment option and follow the steps above. 🚀
