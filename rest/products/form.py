from flask_wtf import FlaskForm
from flask import request
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError

from rest.products.crud import products_storage


def validate_product_name(form, field):
    product_name = field.data
    if request.method == "POST" and products_storage.name_exists(product_name):
        raise ValidationError(f"{product_name} already in list.")
    if not product_name.isalpha():
        raise ValidationError(f"Name must be alphabetical.")


class ProductForm(FlaskForm):
    name = StringField(
        label="Product name",
        validators=[DataRequired(),
                    validate_product_name,]
    )
    price = IntegerField(
        label="Product price",
        validators=[DataRequired(),
                    NumberRange(min=1, max=100_000),
                    ],
    )
    submit = SubmitField(label="Add product")
    update_submit = SubmitField(label="Update product")
