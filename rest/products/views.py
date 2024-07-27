from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.exceptions import BadRequest

from .crud import products_storage


products_app = Blueprint("products_app", __name__)

app = products_app


@app.get("/", endpoint="list")
def get_products_list():
    products = products_storage.get_list()
    return render_template("products/list.html", products=products)


@app.post("/", endpoint="create")
def create_product():
    product_name = request.form.get("product_name", "").strip()
    product_price = request.form.get("product_price", "").strip()
    if product_price.isdigit() and product_name.isalpha():
        products_storage.add(product_name, int(product_price))
    else:
        raise BadRequest
    # для стандартной формы
    # return redirect(url_for("products_app.list"))
    products = products_storage.get_list()
    return render_template(
        "products/components/products_list.html",
        products=products
    )
