from . import bp
from flask import render_template, request
from dataclasses import dataclass


@dataclass()
class Axis:
    name: str
    label: str
    value: int = 0


axes_dict = {f"ax{i}": Axis(name=f"ax{i}", label=f"Achse {i + 1}") for i in range(6)}


@bp.route('/', methods=["GET", "POST"])
def index():
    return render_template("main/index.html", axes=axes_dict.values())


@bp.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        print(request.form)
    return render_template("main/test.html")