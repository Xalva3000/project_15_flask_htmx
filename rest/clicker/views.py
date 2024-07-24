from flask import Blueprint, render_template, request

clicker_app = Blueprint("clicker_app", __name__)

app = clicker_app


@app.get("/", endpoint="index")
def examples_list():
    return render_template("clicker/index.html")