import requests
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=["get"])
def index():
    list = requests.get("https://www.melivecode.com/api/users").json()
    print(list)    
    return render_template("index.html", list=list) 