from filmConnect import *
from readFilmData import readFilms 
from insertFilmData import addFilms
from updateFilmData import updateFilms
from deleteFilmData import deleteFilm

# create a function

def menuOptions():

    options = 0

    while options not in ["1","2","3","4","5"]:
        print("Films Menu Options\nEnter:\n1. To Print.\n2. To Add.\n3. To Update.\n4. To Delete.\n5. To Exit")
        # re-assign a new value to the options variable
        options = input("\nEnter one of the options above: ")
        if options not in ["1", "2", "3", "4", "5"]:
            print(f"{options} is not a valid choice")
    return options

menuOptions()




mainProgram = True

while mainProgram: # == True
    mainmenu = menuOptions()
    if mainmenu == "1":

        cursor.execute("SELECT * FROM films")
        row = cursor.fetchall()
        for record in row:
            print(f"These are all the films recorded: {record}")
        cursor.execute("SELECT * FROM films WHERE genre = 'romance'")
        row = cursor.fetchall()
        for record in row:
            print(f"These are all the films under the genre romance: {record}")

        cursor.execute("SELECT * FROM films WHERE yearReleased = '2004'")
        row = cursor.fetchall()
        for record in row:
            print(f"These are all the films released in the year 2004: {record}")

        cursor.execute("SELECT * FROM films WHERE rating = 6")
        row = cursor.fetchall()
        for record in row:
            print(f"These are films with a 6/10 rating: {record}")
        readFilms()


    elif mainmenu == "2":
        addFilms()
    elif mainmenu == "3":
        updateFilms()
    elif mainmenu == "4":
        deleteFilm()
    else:
        mainProgram = False

input("Press Enter to Exit: ")
