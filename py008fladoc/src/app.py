import os

from flask import Flask, jsonify, request


class UserNotFoundError(Exception):
    pass


app = Flask(__name__)


@app.errorhandler(UserNotFoundError)
def handle_user_not_found(_: UserNotFoundError) -> tuple:
    return jsonify({"result": False, "data": "user not found"}), 404


@app.get("/hello")
def hello() -> tuple:
    # `?user=missing` lets us validate the exception response shape.
    if request.args.get("user") == "missing":
        raise UserNotFoundError()

    return jsonify({"result": True, "data": "hello world 1"}), 200


if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=True)
