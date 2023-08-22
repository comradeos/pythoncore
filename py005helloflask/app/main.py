from flask import Flask, json, Response

companies = [
    { "id": 1, "name": "CompanyA"},
    { "id": 2, "name": "CompanyB"},
]

api = Flask(__name__)


@api.route("/companies", methods=["GET"])
def get_companies():
    data = json.dumps(companies)
    return Response(data, mimetype="application/json")


if __name__ == "__main__":
    api.run()