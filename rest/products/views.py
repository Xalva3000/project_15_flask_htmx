from flask import Blueprint, request, render_template, redirect, url_for, Response
from http import HTTPStatus

from werkzeug.exceptions import HTTPException, NotFound

from .crud import products_storage
from .form import ProductForm

products_app = Blueprint("products_app", __name__)

app = products_app


@app.get("/", endpoint="list")
def get_products_list():
    form = ProductForm()
    products = products_storage.get_list()
    return render_template(
        "products/list.html",
        products=products,
        form=form,
    )


@app.post("/", endpoint="create")
def create_product():
    form = ProductForm()
    if not form.validate_on_submit():
        return render_template(
            "products/components/form.html",
            form=form
        )
    product = products_storage.add(
        name=form.name.data,
        price=form.price.data
    )
    # error = 'Price is digit, name is alphabetical.'
    # error = error,
    # product_name = product_name,
    # product_price = product_price
    # product_name = request.form.get("product_name", "").strip()
    # product_price = request.form.get("product_price", "").strip()
    # if product_price.isdigit() and product_name.isalpha():
    #     product = products_storage.add(product_name, int(product_price))
    # else:


    # , HTTPStatus.UNPROCESSABLE_ENTITY
    # raise HTTPStatus.UnprocessableEntity
    # для стандартной формы
    # return redirect(url_for("products_app.list"))
    # products = products_storage.get_list()
    return render_template(
        "products/components/form_and_product-oob.html",
        product=product,
        form=ProductForm(formdata=None),
    )


@app.get("/<int:product_id>/", endpoint="details")
def get_product_by_id(product_id):
    product = products_storage.get_by_id(product_id)
    if not product:
        raise NotFound(f"Product with id {product_id} does not exist!")
    return render_template(
        "products/details.html",
        product=product
    )


@app.delete("<int:product_id>", endpoint="delete")
def delete_product(product_id):
    products_storage.delete(product_id)
    return Response(status=HTTPStatus.OK) # HTTPStatus.NO_CONTENT

