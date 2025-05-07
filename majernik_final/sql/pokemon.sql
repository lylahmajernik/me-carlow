/*
Lylah Majernik
Programming 2 Final
Submitted 5/7/2025
*/


CREATE TABLE IF NOT EXISTS POKEMON
                    (ID      INTEGER      PRIMARY KEY,
                     Name    TEXT         NOT NULL UNIQUE,
                     Height  INTEGER,
                     Weight  INTEGER,
                     Experience  INTEGER)STRICT
                        