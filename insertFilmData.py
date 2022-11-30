from filmConnect import *
from readFilmData import readFilms
import time

def addFilms():
    films = []

    title = input("Enter Film Name: ")
    yearReleased = input("Enter Release Date: ")
    rating = input("Enter Film Rating /10: ")
    duration = input("Enter Film Duration: ")
    genre = input("Enter Film Genre: ")

    films.append(title)
    films.append(yearReleased)
    films.append(rating)
    films.append(duration)
    films.append(genre)

    cursor.execute("INSERT INTO films VALUES(NULL, ?, ?, ?, ?, ?)", films)
    conn.commit()
    print(f"Film {title} added to the films table")
    time.sleep(2)

    cursor.execute("SELECT * FROM films")
    row = cursor.fetchall()

    for record in row:
        print(record)

    readFilms()

if __name__=="__main__":
    addFilms()





