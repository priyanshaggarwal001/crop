from flask import Flask, request, render_template
import numpy as np
import pickle
import sklearn

print("Scikit-learn version:", sklearn.__version__)

# Load models
dtr = pickle.load(open('dtr.pkl', 'rb'))
preprocessor = pickle.load(open('preprocesser.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Retrieve form inputs and convert to appropriate types
            Year = int(request.form['Year'])
            Rainfall = float(request.form['average_rain_fall_mm_per_year'])
            Pesticides = float(request.form['pesticides_tonnes'])
            Temperature = float(request.form['avg_temp'])
            Area = float(request.form['Area'])
            Crop = request.form['Item']  # Categorical input (string)

            # Create feature array
            features = np.array([[Year, Rainfall, Pesticides, Temperature, Area, Crop]], dtype=object)

            # Preprocess features
            transformed = preprocessor.transform(features)

            # Make prediction
            prediction = dtr.predict(transformed).reshape(1, -1)

            predicted_yield = round(prediction[0][0], 2)

            return render_template('index.html', prediction=f"Estimated Yield: {predicted_yield} tonnes")

        except Exception as e:
            return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True, port=5002)
