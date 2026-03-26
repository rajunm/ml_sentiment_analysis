# 🌟 5-Star Sentiment Analysis AI

A high-performance, lightweight NLP web application that classifies text sentiment into five granular categories. This project is specifically optimized to run within the 512MB RAM limits of cloud platforms like Render by using a distilled **TinyBERT** model and a custom CPU-only PyTorch configuration.

## 🧠 Model Overview
Unlike standard binary (Positive/Negative) classifiers, this app uses the **`elo4/TinyBERT-sentiment-model`**. This model provides a "star-rating" style analysis:

| Label | Sentiment | Emoji |
|-------|-----------|-------|
| LABEL_0 | Very Negative | 😠 |
| LABEL_1 | Negative | 🙁 |
| LABEL_2 | Neutral | 😐 |
| LABEL_3 | Positive | 🙂 |
| LABEL_4 | Very Positive | 🤩 |

## 🛠️ Tech Stack
- **Backend:** Python / Flask
- **Machine Learning:** Hugging Face Transformers / PyTorch (CPU-Optimized)
- **Frontend:** HTML5 / CSS3 / Vanilla JavaScript
- **Testing:** Pytest / Postman

## 📁 Project Structure
```text
/my-project
├── main.py              # Flask API and Model Logic
├── requirements.txt     # Dependency list (CPU-only Torch)
├── conftest.py          # Pytest configuration
├── static/
│   └── style.css        # Frontend styling
├── templates/
│   └── index.html       # Web interface
└── tests/
    └── test_app.py      # Automated Python tests
```
## 🚀 Getting Started
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rajunm/ml_deployment.git

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   #### Install packages
   pip install -r requirements.txt

   #### Set environment variables for Hugging Face in your .env file
   HF_HOME = '[project_root_dir]/hf_cache/'  # project_root_dir such as D:/my_projects/ml_sentiment_analysis
   TRANSFORMERS_CACHE = '[project_root_dir]/hf_cache/' # Backup for older versions

3. **Run the Application:**
   ```bash
   python main.py