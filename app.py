from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/returnjson")
def returnJSON():
    my_dict = {"Name":"Sanket","Surname":"Patil","PRN":"12110053"}
    return json.dumps(my_dict)

@app.route("/count/<int:n>")
def calculation(n):
    n5 = n+5
    return render_template('count.html', n=n,n5=n5)
