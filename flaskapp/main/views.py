from . import bp
from .. import redis_client
from flask import render_template, request, current_app
from dataclasses import dataclass


@dataclass()
class Axis:
    name: str
    label: str
    value: int = 0


axes_dict = {f"ax{i}": Axis(name=f"ax{i}", label=f"Achse {i + 1}") for i in range(6)}


def axes_to_redis():
    for key, ax in axes_dict.items():
        redis_client.set(key, ax.value)

def redis_to_axes():
    for key, ax in axes_dict.items():
        ax.value = redis_client.get(key) or 0

@bp.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        current_app.logger.info(str(request.form))
        for key, value in request.form.items():
            axes_dict[key].value = int(value)
        axes_to_redis()
    else:
        redis_to_axes()
        for ax in axes_dict.values():
            ax.value = redis_client.get(ax.name) or 0
    return render_template("main/index.html", axes=axes_dict.values())


@bp.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        print(request.form)
    return render_template("main/test.html")