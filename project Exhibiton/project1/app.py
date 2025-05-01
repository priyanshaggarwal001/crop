from flask import Flask, request, render_template
import numpy as np
import pickle

# Load the trained model and scalers
model = pickle.load(open('model.pkl', 'rb'))
standard_scaler = pickle.load(open('standscaler.pkl', 'rb'))
minmax_scaler = pickle.load(open('minmaxscaler.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Collect input data from the form
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosphorus'])  # Fixed typo here
        K = float(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['pH'])
        rainfall = float(request.form['Rainfall'])

        # Feature list and preprocessing
        features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
        features_scaled_minmax = minmax_scaler.transform(features)
        features_scaled = standard_scaler.transform(features_scaled_minmax)

        # Make prediction
        prediction = model.predict(features_scaled)

        # Mapping prediction to crop name
        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut",
            6: "Papaya", 7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon",
            11: "Grapes", 12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil",
            16: "Blackgram", 17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas",
            20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        crop = crop_dict.get(prediction[0], None)

        if crop:
            result = f"{crop} is the best crop to be cultivated right there."
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."

        return render_template("index.html", result=result)

    except Exception as e:
        print("Error:", e)
        return render_template("index.html", result="Something went wrong. Please check your input values.")

if __name__ == "__main__":
    app.run(debug=True,port=5001)
