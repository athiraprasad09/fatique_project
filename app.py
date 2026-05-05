from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# ✅ Allow all origins (fix for Netlify)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "service": "Cognitive Fatigue Detection API"
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data or "data" not in data:
            return jsonify({"error": "Missing data"}), 400

        typing_data = data["data"]

        if not isinstance(typing_data, list):
            return jsonify({"error": "Data must be a list"}), 400

        if len(typing_data) == 0:
            return jsonify({
                "prediction": "No Data",
                "avg_delay": 0,
                "sample_count": 0
            })

        avg_delay = sum(typing_data) / len(typing_data)

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
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
