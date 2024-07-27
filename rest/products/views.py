from flask import Blueprint, request, render_template, redirect, url_for, Response
from http import HTTPStatus

from werkzeug.exceptions import HTTPException

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
        product = products_storage.add(product_name, int(product_price))
    else:
        error = 'Price is digit, name is alphabetical.'
        return render_template(
            "products/components/form.html",
            error=error,
            product_name=product_name,
            product_price=product_price
        )

    # , HTTPStatus.UNPROCESSABLE_ENTITY
    # raise HTTPStatus.UnprocessableEntity
    # для стандартной формы
    # return redirect(url_for("products_app.list"))
    # products = products_storage.get_list()
    return render_template(
        "products/components/form_and_product-oob.html",
        product=product
    )
