import sqlite3
import pandas as pd

conn = sqlite3.connect('cricket.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Player_Match;

CREATE TABLE Team (
   Team_id    INTEGER PRIMARY KEY,
   Team_name  TEXT
);

CREATE TABLE Match (
   Match_id    INTEGER PRIMARY KEY,
   Season_id   INTEGER,
   Match_Winner INTEGER,
   Win_Margin   Integer
);

CREATE TABLE Player_match (
   Match_id  INTEGER
   Player_id INTEGER
);

INSERT INTO Team VALUES
  (1,'Chennai Super Kings'),(2,'Delhi Capitals'),
  (3,'Deaccan Charger'),(4,'Delhi Daredevils'),
  (5,'Mumbai Indians'),(6,'Kolkata Knight Riders'),
  (7,'Rajasthan Royals'),(8,'King X1 Punjab');

INSERT INTO Match VALUES
  (1,7,5,35),(2,7,5,22),(3,8,5,45),(4,8,5,8),
  (5,8,1,67),(6,8,6,19),(7,9,5,33),(8,9,1,28),
  (9,9,5,12),(10,9,6,55),(11,9,3,38),(12,9,7,4);

INSERT INTO Player_Match VALUES
  (1,101),(1,102),(2,103),(3,101),(4,104),(5,102);
""")
conn.commit()
print('Database ready!')


tables = pd.read_sql("""SELECT *
    FROM sqlite_master
    Where type='table';""", conn)
print(tables)    