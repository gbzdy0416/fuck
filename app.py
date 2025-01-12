from flask import Flask, redirect, request, render_template
import os
from pickledb import PickleDB

app = Flask(__name__)

db = PickleDB("t.db")

@app.route('/')
def hello_world():  # put application's code here
    return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        pw = request.form["password"]
        db.set('name', username)
        db.set('password', pw)
        db.save()
    return render_template("tmp.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)


@app.route("/check")
def check():
    return render_template("what.html", name = db.get('name'), password=db.get('password'))
