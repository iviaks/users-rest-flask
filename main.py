from flask import Flask
from src.server import api

import src.views.user  # noqa

app = Flask(__name__)
api.init_app(app)
