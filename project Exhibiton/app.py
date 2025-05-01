from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Route for the main dashboard
@app.route('/')
def index():
    return render_template("index.html")  # Main dashboard

# Route for Project 1 (Crop Recommendation)
@app.route('/project1')
def project1():
    return redirect("http://localhost:5001/")  # Redirect to Project 1 app

# Route for Project 2 (Crop Yield Prediction)
@app.route('/project2')
def project2():
    return redirect("http://localhost:5002/")  # Redirect to Project 2 app

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Main app runs on port 5000
