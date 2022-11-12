from sql.sql_connection import engine
import pandas as pd

def get_everything ():
    query = """SELECT * FROM the_office_lines;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_everything_from_character (name):
    query = f"""SELECT * 
    FROM the_office_lines
    WHERE speaker = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_just_dialogue (name):
    query = f"""SELECT line 
    FROM the_office_lines
    WHERE speaker = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")