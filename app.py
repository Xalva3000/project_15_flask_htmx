from flask import Flask
from rest.index import index_app
from rest.examples import examples_app
from rest.clicker import clicker_app
from rest.products import products_app
from csrf_protection import csrf


def create_app():
    app = Flask(__name__)
    app.config.update(
        TEMPLATES_AUTO_RELOAD=True,
        SECRET_KEY='6a3fbef20c610dd301963966b71c36188e70d0866239c83e7e77160ea0281e17',
    )
    csrf.init_app(app)

    app.register_blueprint(index_app)
    app.register_blueprint(
        examples_app,
        url_prefix="/examples",
    )
    app.register_blueprint(
        clicker_app,
        url_prefix="/clicker"
    )
    app.register_blueprint(
        products_app,
        url_prefix="/products"
    )
    return app


def main():
    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
