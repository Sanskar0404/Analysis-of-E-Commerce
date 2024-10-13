import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder="template", static_folder="staticfiles")  # Assign Flask
model = pickle.load(open('build.pkl', 'rb'))  # Import model

@app.route('/')
def home():
    return render_template('index.html')  # Read index.html file

@app.route('/predict', methods=['POST'])  # Transfer data from HTML to Python/server
def predict():
    int_features = [int(x) for x in request.form.values()]  # Request data values
    final_features = [np.array(int_features)]  # Convert into array
    prediction = model.predict(final_features)  # Predict
    
    # Check the prediction result
    if prediction == 0:
        return render_template('index.html', prediction_text="Churn is Not Accepted")
    else:
        return render_template('index.html', prediction_text="Churn is Accepted")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
