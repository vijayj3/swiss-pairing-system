# Swiss Pairing System
This program which is written in python using the libraries psycopg2 (postgresQL DB-API module). Using this program you can pair contenders in a tournament using the swiss pairing system.

### What is a Swiss Pairing System?  
Check this article by [wikipedia](https://en.wikipedia.org/wiki/Swiss-system_tournament)

### Usage
1. Firstly create the new database called 'tournament' and then connect to using `\c tournament`
2. Import [tournament.sql](https://github.com/vijayj3/swiss-pairing-system/blob/master/tournament.sql) using the command `\i tournament.sql`  
3. Run the [tournament.py](https://github.com/vijayj3/swiss-pairing-system/blob/master/tournament.py) file. Make sure that its in the same folder as [tournament.sql](https://github.com/vijayj3/swiss-pairing-system/blob/master/tournament.sql)

### Additional Resources
1. https://www.tutorialspoint.com/postgresql/postgresql_create_database.htm
2. http://www.postgresonline.com/downloads/special_feature/postgresql83_psql_cheatsheet.pdf
3. http://www.davidpashley.com/articles/postgresql-user-administration/
