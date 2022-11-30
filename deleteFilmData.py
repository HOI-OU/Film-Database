from filmConnect import *
from readFilmData import readFilms
import time

def deleteFilm():

    # What field is ideal for deleting a record in the songs table and why ?
    # SongID of the record to be updated
    idField = input("Enter the filmID of the film to be deleted: ")

    cursor.execute(f"DELETE FROM film WHERE filmID={idField}")

    conn.commit()

    # returns the id of the deleted song
    print(f"Record {idField} deleted from the film table")
    time.sleep(2)

    # call/invoke the readSongs from readData
    readFilms()


if __name__=="__main__": # with this, it won't run readSongs if it is not the main file
    deleteFilm()