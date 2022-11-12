DROP DATABASE IF EXISTS the_office;
CREATE DATABASE the_office;
USE the_office;

SET GLOBAL LOCAL_INFILE=1;

DROP TABLE IF exists the_office_lines;
CREATE TABLE the_office_lines(
	id INT NOT NULL PRIMARY KEY,
	season INT, 
	episode INT, 
	title VARCHAR(100),
	scene INT,
	speaker VARCHAR(100),
	line VARCHAR(10000)
);

LOAD DATA LOCAL INFILE '/Users/marcdalmau/Desktop/IRONHACK/projects/project_4/data/the_office_clean.csv' 
INTO TABLE the_office_lines
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, season, episode, title, scene, speaker, line);