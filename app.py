import random
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    if request.method=='POST':
        length = int(request.form['length'])
        password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()<>?"

        output = "".join(random.sample(password, length))

    return render_template("index.html", result=output)
    

if __name__ == "__main__":
    app.run(debug=True)