import sqlite3

conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE genres (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, genre_id INTEGER);
CREATE TABLE actors (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE cast (movie_id INTEGER, actor_id INTEGER);
CREATE TABLE ratings (movie_id INTEGER, user TEXT, score REAL);

INSERT INTO genres (name) VALUES ("Comedy"), ("Drama"), ("Action");
INSERT INTO movies (title, year, genre_id) VALUES ("Inception", 2010, 3), ("Friends", 1994, 1), ("The Godfather", 1972, 2);
INSERT INTO actors (name) VALUES ("Leonardo DiCaprio"), ("Jennifer Aniston"), ("Marlon Brando");
INSERT INTO cast VALUES (1, 1), (2, 2), (3, 3);
INSERT INTO ratings VALUES (1, "user1", 9.5), (1, "user2", 9.0), (2, "user1", 8.0), (3, "user1", 9.7);
""")

conn.commit()
conn.close()