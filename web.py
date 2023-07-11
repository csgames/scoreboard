import os
import re

from flask import Flask, send_file

app = Flask(__name__)


def hello():
    return "Hello world!"


@app.route("/")
@app.route("/index.html")
def return_index():
    try:
        return send_file("index.html")
    except Exception as e:
        return str(e)


@app.route("/result/<year>.json")
def result_competition_list(year):
    if re.match(r"^\d{4}$", year):
        try:
            return send_file("".join(("result/", year, ".json")))
        except Exception as e:
            return str(e)
    return "[]"


@app.route("/result/<year>/<competition>.json")
def result_competition(year, competition):
    if re.match(r"^\d{4}$", year) and "/" not in competition and "." not in competition:
        # show_result = os.getenv('_'.join((year,competition.upper())), False)
        show_result = "true"
        print(show_result)
        if show_result == "true":
            print("hello")
            try:
                return send_file("".join(("result/", year, "/", competition, ".json")))
            except Exception as e:
                return str(e)
    return "[]"


@app.route("/events.json")
def events_json():
    try:
        return send_file("events.json")
    except Exception as e:
        return str(e)


@app.route("/css/bootstrap.min.css")
def boostrap_min_css():
    try:
        return send_file("css/bootstrap.min.css")
    except Exception as e:
        return str(e)


@app.route("/js/registration.css")
def registration_css():
    try:
        return send_file("css/registration.css")
    except Exception as e:
        return str(e)


@app.route("/js/bootstrap.min.js")
def boostrap_min_js():
    try:
        return send_file("js/bootstrap.min.js")
    except Exception as e:
        return str(e)


@app.route("/js/angular.min.js")
def angular_min_js():
    try:
        return send_file("js/angular.min.js")
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
