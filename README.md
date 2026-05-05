# Real-Time Cognitive Fatigue Detection System

A web-based application that monitors typing patterns in real-time to detect cognitive fatigue levels.

## System Architecture

- **Backend**: Flask (Python) REST API
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **ML Model**: Random Forest Classifier (scikit-learn)
- **Detection Logic**: Typing speed analysis based on keystroke intervals

## How It Works

1. User types code in the text area
2. System captures keystroke timing data
3. On "Check Fatigue" click, data is sent to Flask backend
4. Backend calculates average typing delay
5. Returns fatigue classification:
   - **High Fatigue**: avg delay > 500ms
   - **Low Fatigue**: avg delay ≤ 500ms

## Local Deployment

### Prerequisites
- Python 3.8+
- pip

### Installation Steps

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Train the Model** (Optional - creates model.pkl)
```bash
python train.py
```

3. **Start Flask Server**
```bash
python app.py
```
Server runs at: `http://127.0.0.1:5000`

4. **Open Frontend**
   - Open `index.html` in a web browser
   - Or serve it via:
```bash
python -m http.server 8000
```
   - Then navigate to: `http://localhost:8000`

## Project Structure

```
fatigue-detector/
├── app.py              # Flask backend API
├── train.py            # ML model training script
├── index.html          # Frontend interface
├── requirements.txt    # Python dependencies
├── model.pkl          # Trained model (generated)
└── README.md          # This file
```

## API Endpoint

**POST** `/predict`

Request:
```json
{
  "data": [120, 340, 230, 560, 420]  // Array of keystroke intervals in ms
}
```

Response:
```json
{
  "prediction": "High Fatigue"  // or "Low Fatigue" or "No Data"
}
```

## Cloud Deployment Options

### Option 1: Heroku
1. Create `Procfile`:
```
web: python app.py
```
2. Deploy:
```bash
heroku create fatigue-detector
git push heroku main
```

### Option 2: Railway
1. Connect GitHub repo
2. Railway auto-detects Python
3. Set start command: `python app.py`

### Option 3: Render
1. Create new Web Service
2. Build command: `pip install -r requirements.txt`
3. Start command: `python app.py`

### Option 4: DigitalOcean App Platform
1. Connect repo
2. Auto-detected Python build
3. HTTP port: 5000

### Option 5: AWS Elastic Beanstalk
1. Install EB CLI
2. Initialize:
```bash
eb init -p python-3.9 fatigue-detector
eb create fatigue-env
eb open
```

## Production Considerations

1. **CORS Configuration**: Update allowed origins in app.py
2. **Environment Variables**: Move hardcoded values to .env
3. **Model Training**: Use real keystroke dataset
4. **Security**: Add rate limiting, input validation
5. **HTTPS**: Required for production (browsers block mixed content)
6. **Frontend Hosting**: Deploy HTML separately (Netlify, Vercel, Cloudflare Pages)

## Customization

### Adjust Fatigue Threshold
In `app.py`, modify:
```python
if avg_delay > 500:  # Change 500 to desired milliseconds
```

### Enhanced Model
Replace simple threshold logic with trained ML model:
```python
import joblib
model = joblib.load("model.pkl")
result = model.predict([[avg_delay]])[0]
```

## Tech Stack

- **Python 3.x**
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin requests
- **scikit-learn** - Machine learning
- **joblib** - Model serialization

## Future Enhancements

- [ ] Real-time graph visualization
- [ ] Historical fatigue tracking
- [ ] Break time recommendations
- [ ] Integration with IDE extensions
- [ ] Multi-user dashboard
- [ ] Advanced ML features (typing rhythm, error rate, pause patterns)

## License

MIT

## Author

Bread Butter Club - Creative & Technical Studio
