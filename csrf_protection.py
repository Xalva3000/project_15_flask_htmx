from flask_wtf import CSRFProtect
import secrets


csrf = CSRFProtect()


if __name__ == "__main__":
    print(secrets.token_hex())