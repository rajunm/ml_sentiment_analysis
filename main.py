import os
from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)


# 1. Load the pretrained model
sentiment_pipeline = pipeline("sentiment-analysis", low_cpu_mem_usage=True)  # Uses the default model from the hub for sentiment analysis
# sentiment_pipeline = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 2. Extract JSON data from the request
        data = request.get_json()
        print(data, type(data))
        input_text = [data['input_text']]     #["I love you", "I hate you"]

        # 3. Use the model to predict the sentiment of the input text
        output_txt = sentiment_pipeline(input_text)
            
        # 4. Return the result as JSON
        return jsonify({
            'output text': output_txt                        # text_from_ids(input_ids, vocab).numpy().decode('utf-8')
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    # Use the port assigned by the cloud provider, or 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)