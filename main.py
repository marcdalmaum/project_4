# Import libraries
from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
import src.sql_queries as sql
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
app = Flask(__name__)


# Read ME
@app.route("/readme/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])


# GET:
# Get everything
@app.route("/all/")
def all ():
    return jsonify(sql.get_everything())

# Get everything from one episode
@app.route("/episode/<episode>/", )
def everithing_from_episodes (episode):
    return jsonify(sql.get_everything_from_episode(episode))

# Get everything from one character
@app.route("/character/<name>/", )
def everithing_from_characters (name):
    return jsonify(sql.get_everything_from_character(name))

# Get all characters and their total lines
@app.route("/characters/")
def characters ():
    return jsonify(sql.get_characters_and_total_lines())

# Get just dialogues from one episode
@app.route("/lines/episode/<episode>/", )
def lines_from_episodes (episode):
    return jsonify(sql.get_dialogue_from_episode(episode))

# Get the sentiment analysis of each line from one episode
@app.route("/sa/episode/<episode>/", )
def sa_from_episode (episode):
    everything = sql.get_dialogue_from_episode(episode)
    return jsonify([sia.polarity_scores(i["line"])["compound"] for i in everything])

# Get just dialogues from one character
@app.route("/lines/character/<name>/", )
def lines_from_characters (name):
    return jsonify(sql.get_dialogue_from_character(name))

# Get the sentiment analysis of each line from one character
@app.route("/sa/character/<name>/", )
def sa_from_character (name):
    everything = sql.get_dialogue_from_character(name)
    return jsonify([sia.polarity_scores(i["line"])["compound"] for i in everything])


# POST:
@app.route("/insertrow", methods=["POST"])
def try_post ():

    my_params = request.args
    season = my_params["season"]
    episode = my_params["episode"]
    title = my_params["title"]
    scene = my_params["scene"]
    speaker = my_params["speaker"]
    line = my_params["line"] 

    sql.insert_one_row(season, episode, title, scene, speaker, line)
    return f"Query succesfully inserted"


if __name__ == "__main__":
    app.run(port=9000, debug=True)