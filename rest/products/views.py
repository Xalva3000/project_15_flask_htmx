from dataclasses import asdict

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

def get_product(product_id):
    product = products_storage.get_by_id(product_id)
    if product:
        return product
    raise NotFound(f"Product with id {product_id} does not exist!")

@app.get("/<int:product_id>/", endpoint="details")
def get_product_by_id(product_id):
    product = get_product(product_id)
    return render_template(
        "products/details.html",
        product=product,
        form=ProductForm(data=asdict(product))
    )

@app.put("/<int:product_id>/", endpoint="update")
def update_product(product_id):
    product = get_product(product_id)
    form = ProductForm()
    if not form.validate_on_submit():
        return render_template(
            "products/components/form_update.html",
            form=form,
            product=product,
        )
    else:
        products_storage.update(
            product_id=product.id,
            product_name=form.name.data,
            product_price=form.price.data,
        )
        return render_template(
            "products/components/form_update.html",
            form=form,
            product=product,
        )


@app.delete("<int:product_id>", endpoint="delete")
def delete_product(product_id):
    products_storage.delete(product_id)
    if not request.args.get("redirect"):
        return Response(status=HTTPStatus.OK)
    url = url_for("products_app.list")
    return redirect(url, code=HTTPStatus.SEE_OTHER)
    # return Response(status=HTTPStatus.OK) # HTTPStatus.NO_CONTENT

