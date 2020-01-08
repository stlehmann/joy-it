from flask import request, current_app
from . import bp
from .. import redis_client


@bp.route("/get")
def get():
    key = request.args["key"]
    res  = redis_client.get(key)
    if res is None:
        return "None"
    return res


@bp.route("/scan")
def scan():
    cursor = request.args.get("cursor", 0)
    cursor_new, elements = redis_client.scan(cursor)
    return f"{cursor_new})\t{elements}"


@bp.route("/set")
def set():
    key = request.args["key"]
    value = request.args["value"]
    ret = redis_client.set(key, value)
    if ret:
        return "done"
    return "error"
