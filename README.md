# 🌾 Crop Recommendation and Yield Prediction Web App

A machine learning-based web application that helps farmers and agricultural planners determine the **most suitable crop** to grow and **predict the expected yield** based on soil and environmental parameters.

---

## 🔍 Features

- 📈 Predict the best crop to grow based on:
  - Soil nutrients (N, P, K)
  - Temperature
  - Humidity
  - pH level
  - Rainfall
- 📊 Estimate the **expected yield** for the predicted crop.
- 🌐 User-friendly web interface built with **Flask** (or Streamlit/Django – edit accordingly).
- 📁 Trained ML model (Random Forest / XGBoost / etc.)
- 📌 Option to retrain the model using custom CSV data.

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap (or Streamlit UI)
- **Backend**: Python, Flask (or Django)
- **Machine Learning**: scikit-learn, pandas, numpy
- **Model**: Random Forest Classifier + Regression for yield
- **Deployment**: (Optional: Render / Heroku / Streamlit Cloud / AWS)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/crop-prediction-app.git
cd crop-prediction-app

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```
## 🧠 Model Training (Optional)

To retrain the model on custom data:

- python train_model.py


## Ensure your dataset follows this format:

- N, P, K, temperature, humidity, ph, rainfall, label, yield

## 🙌 Acknowledgements

Kaggle Crop Recommendation Dataset
Python ML libraries
Indian agriculture research references

## 🚀 Future Improvements

- Add user authentication
- Include fertilizer recommendations
- Use real-time weather APIs for dynamic predictions
- Deploy as a mobile-friendly PWA

## ✨ Contributors

Made with ❤️ by Priyansh Aggarwal
