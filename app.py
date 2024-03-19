from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/return_json")
def home():
    file_path = 'db.txt'
    with open(file_path, 'r') as file:
        data = file.read()
        return json.loads(data)

    

@app.route("/count/<int:n>")
def calculation(n):
    n5 = n+5;
    return render_template('count.html', n=n,n5=n5)
