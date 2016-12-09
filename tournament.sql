-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE contenders( id SERIAL primary key,
			 names TEXT);

CREATE TABLE points(id INTEGER references contenders,
		    matches INTEGER,
		    wins INTEGER);

CREATE VIEW rankings AS
SELECT contenders.id,contenders.names,points.wins,points.matches 
FROM contenders, points 
WHERE contenders.id = points.id	order by points.wins desc;

