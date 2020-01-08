from flask import Blueprint
bp = Blueprint('redis', __name__, url_prefix="/redis")
from . import views
