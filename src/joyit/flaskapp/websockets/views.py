from .. import socketio, mqtt_wrapper


@socketio.on("move_axis")
def move_axis(json):
    mqtt_wrapper.move_axis(json.axis, json.position, json.velocity)
