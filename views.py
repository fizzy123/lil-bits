import re
import urllib
import logging
import json
import redis
from flask import render_template, request, jsonify, session, redirect, url_for, Response

from server import app
r = redis.Redis()

logger = logging.getLogger(__name__)

@app.route("/internet-fantasy", methods=["GET"])
def internet_fantasy():
    return render_template('internet_fantasy.html')

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/2024_road_trip", methods=["GET"])
def road_trip():
    return render_template('2024_road_trip.html')

@app.route("/css", methods=["GET"])
def css():
    return render_template('css.html')

@app.route("/color", methods=["GET"])
def color():
    return render_template('color.html')

@app.route("/list", methods=["GET"])
def list():
    return render_template('list.html')

@app.route("/list-data", methods=["GET"])
def list_get_data():
    data = r.get('list.data').decode("utf-8")
    return jsonify({"data": data})

@app.route("/list-data", methods=["POST"])
def list_post_data():
    r.set('list.data', request.get_json()["data"])
    return jsonify({"success": True})

@app.route("/food", methods=["GET"])
def food():
    return render_template('food.html')

@app.route("/notifications", methods=["GET"])
def notifications():
    return render_template('notifications.html')

@app.route("/hashtags", methods=["GET"])
def hashtags():
    return render_template('hashtags.html')

@app.route("/api", methods=["GET"])
def api():
    return render_template('api.html')

@app.route("/ritual", methods=["GET"])
def ritual():
    return render_template('ritual.html')

@app.route("/art", methods=["GET"])
def art():
    return render_template('art.html')

@app.route("/gifs", methods=["GET"])
def gifs():
    return render_template('gifs.html')

@app.route("/history", methods=["GET"])
def history():
    return render_template('history.html')

@app.route("/audio", methods=["GET"])
def audio():
    return render_template('audio.html')

@app.route("/social", methods=["GET"])
def social_get():
    return render_template('social.html')

@app.route("/social", methods=["POST"])
def social_post():
    data = request.get_json()
    if not data.get("cheat"):
        r.incr(f"social.real.{data['index']}.{data['realValue']}")
        r.incr(f"social.expected.{data['index']}.{data['expectedValue']}")

    real_counts = {}
    expected_counts = {}
    for i in range(1, 6):
        real_count = r.get(f"social.real.{data['index']}.{i}")
        if not real_count:
            real_count = b"0"
        real_counts[str(i)] = float(real_count.decode("utf-8"))
        expected_count = r.get(f"social.expected.{data['index']}.{i}")
        if not expected_count:
            expected_count = b"0"
        expected_counts[str(i)] = float(expected_count.decode("utf-8"))
    return jsonify({"real": real_counts, "expected": expected_counts})

@app.route("/spotify_lyrics", methods=["GET"])
def spotify_lyrics():
    return render_template('spotify_lyrics.html')

