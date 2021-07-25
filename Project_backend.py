# backend
import sqlite3

check = 1

def foreignkeyon():
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("""PRAGMA foreign_keys = ON""")
    conn.commit()
    conn.close()

def MovieData():
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS movie (Movie_ID INTEGER NOT NULL PRIMARY KEY ,Movie_Name TEXT,Release_Date TEXT,Genre TEXT,Budget TEXT,Duration TEXT,Rating TEXT)""")
    conn.commit()
    conn.close()


def Cast():
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS cast (Movie_id INTEGER NOT NULL ,Actor_name TEXT,DOB TEXT,FOREIGN KEY (Movie_id) REFERENCES movie (Movie_id))""")
    conn.commit()
    conn.close()


def Director():
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS director (Movie_id INTEGER NOT NULL ,Director_name TEXT,DOB TEXT,FOREIGN KEY (Movie_id) REFERENCES movie (Movie_id))""")
    conn.commit()
    conn.close()


def check_movieid(Movie_ID=""):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM movie WHERE Movie_ID=?", (Movie_ID,))
    rows = cur.fetchall()
    conn.close()
    if(len(rows)==0):
        return 1
    else:
        return 0

def AddMovieRec(Movie_ID, Movie_Name, Genre, Release_Date, Budget, Duration, Rating):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO movie VALUES (?,?,?,?,?,?,?)", (Movie_ID,Movie_Name, Genre,Release_Date, Budget, Duration, Rating))
    conn.commit()
    conn.close()


def ViewMovieData():
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM movie")
    rows = cur.fetchall()
    conn.close()
    return rows


def DeleteMovieRec(Movie_ID):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM movie WHERE Movie_ID=?", (Movie_ID,))
    conn.commit()
    conn.close()


def SearchMovieData(Movie_ID=""):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM movie WHERE Movie_ID=?", (Movie_ID,))
    rows = cur.fetchall()
    conn.close()
    return rows


def UpdateMovieData(Movie_ID="", Movie_Name="",Genre="",Release_Date="",  Budget="", Duration="", Rating=""):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("UPDATE movie SET Movie_ID=?,Movie_Name=?,Genre=?,Release_Date=?,Budget=?,Duration=?,Rating=?, WHERE Movie_ID=?",(Movie_ID, Movie_Name,Genre, Release_Date, Budget, Duration, Rating))
    conn.commit()
    conn.close()


def AddCastData(Movie_ID, Actor_name, DOB):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO cast VALUES (?,?,?)", (Movie_ID, Actor_name, DOB))
    conn.commit()
    conn.close()


def SearchCastData(Movie_ID):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cast WHERE Movie_ID=?", (Movie_ID,))
    rows = cur.fetchall()
    conn.close()
    return rows

def ViewCastData():
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cast")
    rows = cur.fetchall()
    conn.close()
    return rows


def DeleteCastData(Movie_ID):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM cast WHERE Movie_ID=?", (Movie_ID,))
    conn.commit()
    conn.close()


def AddDirectorData(Movie_ID, Director_name, DOB):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO director VALUES (?,?,?)",(Movie_ID, Director_name, DOB))
    conn.commit()
    conn.close()

def SearchDirectorData(Movie_ID):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM director WHERE Movie_ID=?", (Movie_ID,))
    rows = cur.fetchall()
    conn.close()
    return rows

def ViewDirectorData():
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM director")
    rows = cur.fetchall()
    conn.close()
    return rows

def DeleteDirectorData(Movie_ID):
    conn = sqlite3.connect("movie1.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM director WHERE Movie_ID=?", (Movie_ID,))
    conn.commit()
    conn.close()
