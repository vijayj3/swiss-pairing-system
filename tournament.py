#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import math


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    i = 0
    c.execute("update points set matches = 0,wins = 0")
    db.commit()
    db.close
    
def deletePlayers():
    """Remove all the player records from the database."""
    deleteMatches()
    db = connect()
    c = db.cursor()
    c.execute("delete from points")
    db.commit()
    c.execute("delete from contenders")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("select count(names) as sum from contenders")
    num = c.fetchall()[0][0]
    db.close()
    return num


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    c.execute("insert into contenders(names) values(%s)",(name,))
    db.commit()
    c.execute("select id from contenders order by id desc limit 1")
    res_id = c.fetchall()[0][0]
    c.execute("insert into points(id,matches,wins) values(%d,0,0)" %res_id)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    c.execute("select * from rankings")
    results1 = c.fetchall()
    db.close()
    return results1

    
def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    query = "select matches,wins from points where id = %d"
    c.execute(query % winner)
    results = c.fetchone()
    matches = results[0]
    wins = results[1]
    query2 = "update points set matches=%d, wins = %d where id =%d"
    c.execute(query2 % (matches+1,wins+1,winner))
    db.commit()
    c.execute(query % loser)
    results = c.fetchone()
    matches = results[0]
    wins = results[1]
    c.execute(query2 % (matches+1,wins,loser))
    db.commit()
    db.close()
    
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    count = countPlayers()/2
    db = connect()
    c = db.cursor()
    c.execute("create table nextround(aid integer, aname text, bid integer, bname text);")
    db.commit()
    i = 0
    while (i<count):
    	c.execute("insert into nextround select a.id,a.names,b.id,b.names from rankings as a, rankings as b where a.id!=b.id and a.id not in (select aid from nextround) and a.id not in(select bid from nextround) and b.id not in (select aid from nextround) and b.id not in (select bid from nextround) and a.wins = b.wins limit 1")
    	db.commit()
    	i = i+1;
    c.execute("select * from nextround")
    results = c.fetchall()
    c.execute("drop table nextround;")
    db.commit()
    db.close()
    return results

def show_output():
	db = connect()
	c = db.cursor()
	query = "select * from contenders"
	c.execute(query)
	results1 = c.fetchall()
	c.execute("select * from points")
	results2 = c.fetchall()
	db.close
	return results1,results2

