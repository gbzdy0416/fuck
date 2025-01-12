from flask import Flask, redirect, request, render_template
import bcrypt
import os
import string
import subprocess
import socket

app = Flask(__name__)

if not os.path.exists("app-secret.key"):
    with open("app-secret.key", "wb") as f:
        f.write(b"name and password inside:\n")


@app.route('/')
def hello_world():  # put application's code here
    return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        pw = request.form["password"]
        with open("app-secret.key", "wb") as f:
            f.write((username + "\n" + pw).encode())
    return render_template("tmp.html")


if __name__ == '__main__':
    app.run()


@app.route("/check", methods=["GET"])
def check():
    if not os.path.exists("app-secret.key"):
        return render_template("check.html", ln="invalid!")
    with open("app-secret.key", "rb") as f:
        things = f.read()
    return render_template("check.html", ln=things)
