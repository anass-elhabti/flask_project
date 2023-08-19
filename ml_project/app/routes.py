from flask import render_template, request
from app import app

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    return render_template('index.html')

