from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Configure CORS - restrict in production
CORS(app, resources={
    r"/predict": {
        "origins": os.getenv("ALLOWED_ORIGINS", "*").split(",")
    }
})

@app.route("/", methods=["GET"])
def home():
    """Health check endpoint"""
    return jsonify({
        "status": "online",
        "service": "Cognitive Fatigue Detection API",
        "version": "1.0.0"
    })

@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict fatigue level based on typing data
    
    Request body:
    {
        "data": [120, 340, 230, 560, 420]  // keystroke intervals in milliseconds
    }
    
    Response:
    {
        "prediction": "High Fatigue" | "Low Fatigue" | "No Data",
        "avg_delay": 334.0,
        "sample_count": 5
    }
    """
    try:
        data = request.get_json()
        
        if not data or "data" not in data:
            return jsonify({
                "error": "Missing 'data' field in request body"
            }), 400
        
        typing_data = data["data"]
        
        if not isinstance(typing_data, list):
            return jsonify({
                "error": "'data' must be an array of numbers"
            }), 400
        
        if len(typing_data) == 0:
            return jsonify({
                "prediction": "No Data",
                "avg_delay": 0,
                "sample_count": 0
            })
        
        # Calculate average typing delay
        avg_delay = sum(typing_data) / len(typing_data)
        
        # Fatigue classification logic
        # Threshold: 500ms (can be tuned based on real data)
        if avg_delay > 500:
            result = "High Fatigue"
        else:
            result = "Low Fatigue"
        
        return jsonify({
            "prediction": result,
            "avg_delay": round(avg_delay, 2),
            "sample_count": len(typing_data)
        })
    
    except Exception as e:
        return jsonify({
            "error": "Internal server error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV") == "development"
    
    app.run(
        host="0.0.0.0",
        port=port,
        debug=debug
    )
