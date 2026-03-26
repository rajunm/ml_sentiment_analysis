from dotenv import load_dotenv
import os

# This looks for the .env file and sets the variables
load_dotenv()

from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)


# 1. Load the pretrained model
# sentiment_pipeline = pipeline("sentiment-analysis")  # Uses the default 
sentiment_pipeline = pipeline("sentiment-analysis", model="elo4/TinyBERT-sentiment-model") 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json['text']
        if not data:
            return jsonify({"error": "No text provided"}), 400

        # 2. Get prediction from model
        #print(data)
        result = sentiment_pipeline(data)[0]
        
        # 3. Map internal labels to the strings expected by your HTML/JS
        # LABEL_0 = 1 star (Very Neg), LABEL_4 = 5 stars (Very Pos)
        label_map = {
            "LABEL_0": "Very Negative",
            "LABEL_1": "Negative",
            "LABEL_2": "Neutral",
            "LABEL_3": "Positive",
            "LABEL_4": "Very Positive"
        }
        
        friendly_label = label_map.get(result['label'], "Unknown")
        
        return jsonify({
            "label": friendly_label,
            "score": float(result['score'])
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Use the port assigned by the cloud provider, or 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)