from flask import Flask, render_template
import json
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per day"],
    storage_uri="memory://",
)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("<string:key>/<string:password>/returnjson")
@limiter.limit("10 per day")
def returnJSON(key,password):
    with open('keys.txt', 'r') as k_file:
        k_data = k_file.read()
        k_my_dict = json.loads(k_data)
        if key not in k_my_dict:
            return "Invalid Key"
        else:
            if password != k_my_dict[key]:
                return "Invalid Password"
    with open('db.txt', 'r') as file:
        data = file.read()
        return json.loads(data)


@app.route("<string:key>/<string:password>/objects")
@limiter.limit("10 per day")
def returnObjects(key, password):
    with open('keys.txt', 'r') as k_file:
        k_data = k_file.read()
        k_my_dict = json.loads(k_data)
        if key not in k_my_dict:
            return "Invalid Key"
        else:
            if password != k_my_dict[key]:
                return "Invalid Password"
    with open('db.txt', 'r') as file:
        data = file.read()
        my_dict = json.loads(data)
        keysList = list(my_dict.keys())
        answer = {
            "No of Objects" : len(keysList),
            "Objects" : keysList
        }
        return json.loads(json.dumps(answer))


@app.route("<string:key>/<string:password>/get_object/<string:obj_name>")
@limiter.limit("10 per day")
def getObject(key, password,obj_name):
    with open('keys.txt', 'r') as k_file:
        k_data = k_file.read()
        k_my_dict = json.loads(k_data)
        if key not in k_my_dict:
            return "Invalid Key"
        else:
            if password != k_my_dict[key]:
                return "Invalid Password"
    with open('db.txt', 'r') as file:
        data = file.read()
        my_dict = json.loads(data)
        if obj_name not in my_dict:
            return json.loads(json.dumps({"status": -1}))
        dict2 = my_dict[obj_name]
        return json.loads(json.dumps(dict2))


@app.route("<string:key>/<string:password>/exists/<string:obj_name>")
@limiter.limit("10 per day")
def existsObject(key, password,obj_name):
    with open('keys.txt', 'r') as k_file:
        k_data = k_file.read()
        k_my_dict = json.loads(k_data)
        if key not in k_my_dict:
            return "Invalid Key"
        else:
            if password != k_my_dict[key]:
                return "Invalid Password"
    with open('db.txt', 'r') as file:
        data = file.read()
        my_dict = json.loads(data)
        if obj_name in my_dict:
            return json.loads(json.dumps({"status" : 1}))
        else:
            return json.loads(json.dumps({"status":-1}))


@app.route("<string:key>/<string:password>/count/<string:obj_name>")
@limiter.limit("10 per day")
def countEntities(key, password, obj_name):
    with open('keys.txt', 'r') as k_file:
        k_data = k_file.read()
        k_my_dict = json.loads(k_data)
        if key not in k_my_dict:
            return "Invalid Key"
        else:
            if password != k_my_dict[key]:
                return "Invalid Password"
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


# @app.route("/count/<int:n>")
# def calculation(n):
#     n5 = n+5
#     return render_template('count.html', n=n,n5=n5)
