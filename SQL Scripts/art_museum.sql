DROP DATABASE IF EXISTS ART_MUSEUM;
CREATE DATABASE ART_MUSEUM; 
USE ART_MUSEUM;

DROP TABLE IF EXISTS art_object;
CREATE TABLE art_object (
    ID_no               INTEGER NOT NULL,
    Title               VARCHAR(255) NOT NULL,
    Descrip             VARCHAR(255) NOT NULL,
    year_created        VARCHAR(30) DEFAULT 'UNKNOWN',
    Epoch               VARCHAR(30) NOT NULL,
    Country_of_origin   VARCHAR(30) NOT NULL,
    Artist              VARCHAR(30) DEFAULT 'UNKNOWN'
    PRIMARY KEY (ID_no),
    FOREIGN KEY (Artist_first) REFERENCES ARTIST(PK_name)
);

DROP TABLE IF EXISTS painting;
CREATE TABLE painting (
    ID_no               INTEGER NOT NULL,
    Paint_type          VARCHAR(30) NOT NULL,
    Drawn_on            VARCHAR(30) NOT NULL,
    Style               VARCHAR(30) NOT NULL
    PRIMARY KEY (ID_no),
    FOREIGN KEY (ID_no) REFERENCES art_object(ID_no)    
);

DROP TABLE IF EXISTS other;
CREATE TABLE other(
    ID_no               INTEGER NOT NULL,
    Otype               VARCHAR(30) NOT NULL,
    Style               VARCHAR(30) NOT NULL
    PRIMARY KEY (ID_no),
    FOREIGN KEY (ID_no) REFERENCES art_object(ID_no)
);



DROP TABLE IF EXISTS artist;
CREATE TABLE artist(
    Fname               VARCHAR(30) NOT NULL,
    Lname               VARCHAR(30) NOT NULL,
    Date_born           VARCHAR(30) DEFAULT 'UNKNOWN',
    Date_died           VARCHAR(30) DEFAULT 'UNKNOWN',
    Country_of_origin   VARCHAR(30) NOT NULL,
    Epoch               VARCHAR(30) NOT NULL,
    Main_stlye          VARCHAR(30) NOT NULL,
    Descrip             VARCHAR(255) NOT NULL
    CONSTRAINT PK_name PRIMARY KEY (Fname, Lname);
);



DROP TABLE IF EXISTS sculpture;
CREATE TABLE sculpture(
    ID_no               INTEGER NOT NULL,
    Material            VARCHAR(30) NOT NULL,
    Height              REAL NOT NULL,
    "Weight"            REAL NOT NULL,
    Style               VARCHAR(30) NOT NULL
    PRIMARY KEY (ID_no),
    FOREIGN KEY (ID_no) REFERENCES art_object(ID_no)
);



DROP TABLE IF EXISTS statue;
CREATE TABLE statue(
    ID_no               INTEGER NOT NULL,
    Material            VARCHAR(30) NOT NULL,
    Height              REAL NOT NULL,
    "Weight"            REAL NOT NULL,
    Style               VARCHAR(30) NOT NULL
    PRIMARY KEY (ID_no),
    FOREIGN KEY (ID_no) REFERENCES art_object(ID_no)
);



DROP TABLE IF EXISTS permanent_collection
CREATE TABLE permanent_collection(
    ID_no               INTEGER NOT NULL,
    Date_acquired       VARCHAR(30) NOT NULL,
    "Status"            VARCHAR("zero" or "one") NOT NULL,
    Cost                REAL NOT NULL
    PRIMARY KEY (ID_no) REFERENCES art_object(ID_no)
);



