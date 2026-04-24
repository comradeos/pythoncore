from flask import Flask, abort, jsonify

app = Flask(__name__)


def _measurements_for(device_id):
    seed = sum(ord(char) for char in device_id)
    voltage = round(20.0 + (seed % 150) / 10, 2)
    current = round(10.0 + (seed % 90) / 3, 2)
    return voltage, current


@app.get("/device/<device_id>")
def device(device_id):
    if device_id.startswith("fail-"):
        abort(404, description="Device not found")

    voltage, current = _measurements_for(device_id)
    return jsonify(
        {
            "device_id": device_id,
            "voltage": voltage,
            "current": current,
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
