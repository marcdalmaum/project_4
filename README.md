# THE OFFICE API PROJECT

<img src="/images/the_office.png">

## OBJECTIVE

The main objective of this project is to create an API with a database of The Office series, in order to perform queries and obtain information.

## ACQUISITION

To perform the analysis, a CSV with the dialogues of The Office series was obtained from [Kaggle](https://www.kaggle.com/datasets/fabriziocominetti/the-office-lines).

## CLEANING

In order to clean the dataframe, simple functions have been used, saved in the [clean_csv.py](data/clean_csv.py) document.

## UPLOAD TO SQL

In order to upload it to sql the following code has been used, saved in the [create_db.sql](data/create_db.sql) document.

## SQL CONNECTION & QUERIES

Once the database was created in MySQL, the connection was made with the [sql_connection.py](src/sql_connection.py) document and then, different functions with queries to the database were created in [sql_queries.py](src/sql_queries.py) document which are used in the [main.py](main.py) document.

## REQUESTS

Finally, some get queries and a sample post query have been performed on the document [requests.ipynb](src/requests.ipynb).

<img src="/images/post_query.png">