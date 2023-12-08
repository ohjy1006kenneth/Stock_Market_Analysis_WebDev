from flask import Flask, render_template, url_for, request
import math;

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('search.html')

@app.route('/', methods=["GET", "POST"])

def result():
    if request.method == 'POST':
        stock_symbol = request.form["stock_symbol"]

        fetch_data(stock_symbol)

    return render_template('result.html', stock_symbol = stock_symbol)

def fetch_data(stock_symbol):
    return None

def predict():
    return None;

if (__name__ == "__main__"):
    app.run(debug=True)