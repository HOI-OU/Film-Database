from filmConnect import *

cursor.execute(
    """ 

CREATE TABLE films (
	"filmID" INTEGER NOT NULL UNIQUE,
	"title" TEXT,
	"yearReleased" DATE,
	"rating" TEXT,
	"durationMin" INTEGER,
	"genre" TEXT,
    PRIMARY KEY("filmID" AUTOINCREMENT)
);"""
)