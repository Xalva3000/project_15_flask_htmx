from flask import Blueprint, render_template, request
from .crud import ClickerRepository

clicker_app = Blueprint("clicker_app", __name__)

app = clicker_app

clicker = ClickerRepository()



@app.route("/", methods=['GET', 'POST'], endpoint="index")
def clicker_handler():
    template_name = "clicker/index.html"
    if bool(request.headers.get('Hx-Request')):
        if request.method == "GET":
            template_name = "clicker/components/clicker_body.html"
        else:
            template_name = "clicker/components/click_count.html"
    if request.method == "GET":
        count = clicker.counter
        return render_template(template_name, count=count)
    else:
        count = clicker.increase()
        return render_template(template_name, count=count)


