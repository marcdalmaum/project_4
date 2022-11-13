from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
import sql.sql_queries as sql
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

app = Flask(__name__)

# Render the markdwon
@app.route("/readme/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])


# GET:
# SQL get everything
@app.route("/all/")
def all ():
    return jsonify(sql.get_everything())

# SQL get everything from one character
@app.route("/<name>/", )
def everithing_from_characters (name):
    return jsonify(sql.get_everything_from_character(name))

# SQL get just dialogues from one character
@app.route("/lines/<name>/", )
def lines_from_characters (name):
    return jsonify(sql.get_just_dialogue(name))

# SQL get the mean of sentiment analysis of each line from one character
@app.route("/sa/<name>/", )
def sa_from_character (name):
    everything = sql.get_just_dialogue(name)
    return jsonify(np.mean([sia.polarity_scores(i["line"])["compound"] for i in everything]))

# SQL get all characters and their total lines
@app.route("/characters/")
def characters ():
    return jsonify(sql.get_characters())


# POST:







if __name__ == "__main__":
    app.run(port=9000, debug=True)