from flask import Blueprint
bp = Blueprint('websockets', __name__)
from . import views