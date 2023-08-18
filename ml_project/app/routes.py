from flask import render_template, request
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    user_input = request.form['user_input']
    
    # Use your machine learning model for prediction
    prediction = your_model.predict(user_input)
    
    return render_template('result.html', prediction=prediction)
