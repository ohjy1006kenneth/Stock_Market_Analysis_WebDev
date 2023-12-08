from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
    return render_template('index.html')

def fetch_data():
    return None

def predict():
    return None;

def rmse():
    return None;

def mape():
    return None;

if (__name__ == "__main__"):
    app.run(debug=True)