from filmConnect import *

def readFilms():
    cursor.execute("SELECT * FROM films")
    row = cursor.fetchall()

    for record in row:
        print(record)

if __name__=="__main__":
    readFilms()