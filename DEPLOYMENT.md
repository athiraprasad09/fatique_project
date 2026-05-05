# 🚀 Deployment Guide - Cognitive Fatigue Detector

## Quick Start (Local)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Train model
python train.py

# 3. Start server
python app.py

# 4. Open index.html in browser
# Or serve it:
python -m http.server 8000
```

---

## 🌐 Cloud Deployment Options

### 1. **Render** (Recommended - Free Tier Available)

**Steps:**
1. Push code to GitHub
2. Go to https://render.com
3. Click "New +" → "Web Service"
4. Connect your repository
5. Configure:
   - **Build Command**: `pip install -r requirements.txt && python train.py`
   - **Start Command**: `python app.py`
   - **Environment**: Python 3
6. Add environment variable:
   - `ALLOWED_ORIGINS` = `*` (or your frontend domain)
7. Deploy

**Frontend on Render:**
1. Click "New +" → "Static Site"
2. Connect repository
3. Set publish directory: `.`
4. Deploy

**Cost**: Free tier available

---

### 2. **Railway** (Easiest Setup)

**Steps:**
1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub"
3. Select your repository
4. Railway auto-detects Python
5. Add environment variables if needed
6. Deploy

**Cost**: $5/month after free trial

---

### 3. **Heroku**

**Steps:**
```bash
# Install Heroku CLI
curl https://cli-assets.heroku.com/install.sh | sh

# Login
heroku login

# Create app
heroku create fatigue-detector-app

# Deploy
git push heroku main

# Open
heroku open
```

**Frontend Setup:**
- Deploy `index.html` to Netlify/Vercel
- Update API endpoint in HTML to Heroku URL

**Cost**: ~$7/month (no free tier anymore)

---

### 4. **Vercel** (Frontend) + **Railway** (Backend)

**Backend on Railway:**
1. Deploy Python app on Railway (see Railway section)
2. Note the deployment URL

**Frontend on Vercel:**
1. Go to https://vercel.com
2. Import your repository
3. Deploy
4. Update `index.html` fetch URL to Railway backend

**Cost**: Free for both

---

### 5. **DigitalOcean App Platform**

**Steps:**
1. Go to https://cloud.digitalocean.com/apps
2. Click "Create App"
3. Connect GitHub repository
4. Configure:
   - **Type**: Web Service
   - **Build Command**: `pip install -r requirements.txt && python train.py`
   - **Run Command**: `python app.py`
   - **Port**: 5000
5. Deploy

**Cost**: $5/month minimum

---

### 6. **AWS Elastic Beanstalk**

**Steps:**
```bash
# Install EB CLI
pip install awsebcli

# Initialize
eb init -p python-3.11 fatigue-detector

# Create environment
eb create fatigue-env

# Deploy
eb deploy

# Open
eb open
```

**Cost**: Pay-as-you-go (can be free tier eligible)

---

### 7. **Google Cloud Run** (Serverless)

**Steps:**
```bash
# Build container
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/fatigue-detector

# Deploy
gcloud run deploy fatigue-detector \
  --image gcr.io/YOUR_PROJECT_ID/fatigue-detector \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

**Cost**: Pay per request (generous free tier)

---

### 8. **Docker Deployment** (Self-Hosted)

**Steps:**
```bash
# Build image
docker build -t fatigue-detector .

# Run container
docker run -p 5000:5000 fatigue-detector

# Or use docker-compose
docker-compose up -d
```

**For Production VPS (DigitalOcean Droplet, Linode, AWS EC2):**
```bash
# SSH into server
ssh user@your-server-ip

# Clone repo
git clone https://github.com/yourusername/fatigue-detector.git
cd fatigue-detector

# Run with docker-compose
docker-compose up -d

# Setup nginx reverse proxy
sudo nano /etc/nginx/sites-available/fatigue-detector
```

**Nginx Config:**
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## 🔒 Production Checklist

Before deploying to production:

- [ ] Update CORS settings in `app.py` (restrict origins)
- [ ] Add rate limiting (Flask-Limiter)
- [ ] Enable HTTPS (Let's Encrypt / Cloudflare)
- [ ] Set up environment variables (.env file)
- [ ] Add logging (Flask logging / Sentry)
- [ ] Implement user authentication (if needed)
- [ ] Add database for storing results (PostgreSQL / MongoDB)
- [ ] Set up monitoring (Uptime Robot / New Relic)
- [ ] Add input validation & sanitization
- [ ] Create backup strategy
- [ ] Document API endpoints (Swagger/OpenAPI)

---

## 🧪 Testing the Deployment

After deployment, test with:

```bash
# Health check
curl https://your-domain.com/

# Test prediction
curl -X POST https://your-domain.com/predict \
  -H "Content-Type: application/json" \
  -d '{"data": [120, 340, 230, 560, 420]}'
```

Expected response:
```json
{
  "prediction": "Low Fatigue",
  "avg_delay": 334.0,
  "sample_count": 5
}
```

---

## 📊 Monitoring

**Recommended Tools:**
- **Uptime**: Uptime Robot (free)
- **Errors**: Sentry (free tier)
- **Analytics**: Google Analytics
- **Logs**: Logtail / Papertrail

---

## 🆘 Troubleshooting

**Issue**: CORS errors
- **Solution**: Add frontend domain to `ALLOWED_ORIGINS` in backend

**Issue**: 502 Bad Gateway
- **Solution**: Check if Flask is binding to `0.0.0.0` not `127.0.0.1`

**Issue**: Module not found errors
- **Solution**: Ensure `requirements.txt` has all dependencies

**Issue**: Model not found
- **Solution**: Run `python train.py` during build process

---

## 📞 Support

For deployment assistance:
- GitHub Issues: [Your Repo URL]
- Email: contact@breadbutterclub.com
- Developed by: **Bread Butter Club**

---

## 📈 Scaling Considerations

As traffic grows:

1. **Add Redis** for caching predictions
2. **Use Celery** for async processing
3. **Implement CDN** (Cloudflare) for static assets
4. **Database** for historical data
5. **Load balancer** for multiple instances
6. **Kubernetes** for container orchestration

---

Made with precision by **Bread Butter Club** 🍞🧈
