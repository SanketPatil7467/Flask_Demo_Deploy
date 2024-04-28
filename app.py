from flask import Flask, render_template
from urllib.parse import urlencode
from urllib.parse import parse_qs
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
    with open('db.txt', 'r') as file:
        data = file.read()
        return json.loads(data)


@app.route("/objects")
def returnObjects():
    with open('db.txt', 'r') as file:
        data = file.read()
        my_dict = json.loads(data)
        keysList = list(my_dict.keys())
        answer = {
            "No of Objects" : len(keysList),
            "Objects" : keysList
        }
        return json.loads(json.dumps(answer))

@app.route("/get_object/<string:obj_name>")
def getObject(obj_name):
    with open('db.txt', 'r') as file:
        data = file.read()
        my_dict = json.loads(data)
        dict2 = my_dict[obj_name]
        return json.loads(json.dumps(dict2))


@app.route("/count/<string:obj_name>")
def countEntities(obj_name):
    with open('db.txt', 'r') as file:
        data = file.read()
        my_dict = json.loads(data)
        if obj_name not in my_dict:
            return json.loads(json.dumps({"status": -1}))
        dict2 = my_dict[obj_name]
        count = len(dict2)
        answer = {
            "entities":count
        }
        return json.loads(json.dumps(answer))


@app.route("/count/<int:n>")
def calculation(n):
    n5 = n+5
    return render_template('count.html', n=n,n5=n5)
