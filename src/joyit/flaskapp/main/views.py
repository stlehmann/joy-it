from dataclasses import dataclass

from flask import render_template, request

from . import bp
from .. import mqtt_wrapper


@dataclass()
class Axis:
    id: int
    name: str
    label: str
    value: int = 0


axes_dict = {f"ax{i}": Axis(id=i, name=f"ax{i}", label=f"Achse {i + 1}") for i in range(6)}


@bp.route('/', methods=["GET", "POST"])
def index() -> str:
    if request.method == "POST":
        axes_vals = map(int, (request.form[key] for key in axes_dict.keys()))
        mqtt_wrapper.move(*axes_vals, 10)

    return render_template("main/index.html", axes=axes_dict.values())
