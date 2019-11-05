CREATE SCHEMA `music` DEFAULT CHARACTER SET utf8;

CREATE TABLE music.artist (

	id INTEGER PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL
);

CREATE TABLE music.album (

	id INTEGER PRIMARY KEY,
    `name` VARCHAR(255),
    artist_id INTEGER,
    `year` INTEGER NOT NULL,
    
    FOREIGN KEY (artist_id) REFERENCES artist(id)
);

CREATE TABLE music.song (

	id INTEGER PRIMARY KEY,
    `name` VARCHAR (255),
    album_id INTEGER,
    length INTEGER NOT NULL,
    track_number INTEGER NOT NULL,
    
    FOREIGN KEY (album_id) REFERENCES album(id)
);