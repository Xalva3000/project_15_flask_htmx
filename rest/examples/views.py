from flask import Blueprint, render_template

examples_app = Blueprint("examples_app", __name__)

app = examples_app


@app.get("/", endpoint="index")
def examples_list():
    return render_template("examples/index.html")
