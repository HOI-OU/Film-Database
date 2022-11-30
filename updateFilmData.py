from filmConnect import *
from readFilmData import readFilms
import time

def updateFilms():
    idField = input("Enter filmID of the film to be updated: ")
    fieldName = input("Which field would you like to update (title/yearReleased/rating/duration/genre?): ")

    newFieldValue = input(f"Enter the new value for the field: {fieldName} ")
    print(f"The new field value entered is {newFieldValue}")

    newFieldValue ="'" + newFieldValue + "'"
    print(f"The new field value entered is {newFieldValue}")


    cursor.execute(f"UPDATE films SET {fieldName} = {newFieldValue} WHERE filmID = {idField}")

    conn.commit()

    print(f"Record {idField} added to films table")
    time.sleep(2)

    readFilms()

if __name__=="__main__":
    updateFilms()