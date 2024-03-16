from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/home")
def home():
    return render_template('home.html')
