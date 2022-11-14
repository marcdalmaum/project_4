# Import libraries
from src.sql_connection import engine
import pandas as pd

# GET QUERIES:
# Get everything
def get_everything ():
    
    query = """SELECT * FROM the_office_lines;"""
    
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# Get everything from one episode
def get_everything_from_episode (episode):
    
    query = f"""SELECT * 
    FROM the_office_lines
    WHERE title = '{episode}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# Get everything from one character
def get_everything_from_character (name):
    
    query = f"""SELECT * 
    FROM the_office_lines
    WHERE speaker = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# Get all characters and their total lines
def get_characters_and_total_lines ():
    
    query = f"""SELECT speaker, COUNT(*) AS total_lines
    FROM the_office_lines 
    GROUP BY speaker
    ORDER BY total_lines DESC"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# Get just dialogues from one episode
def get_dialogue_from_episode (episode):
   
    query = f"""SELECT line 
    FROM the_office_lines
    WHERE title = '{episode}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# Get just dialogues from one character
def get_dialogue_from_character (name):
   
    query = f"""SELECT line 
    FROM the_office_lines
    WHERE speaker = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


# POST QUERY:
def insert_one_row (season, episode, title, scene, speaker, line):
    query = f"""INSERT INTO the_office_lines
     (season, episode, title, scene, speaker, line) 
        VALUES ({season}, {episode}, '{title}', {scene}, '{speaker}', '{line}');
    """
    engine.execute(query)
    return f"Correctly introduced!"