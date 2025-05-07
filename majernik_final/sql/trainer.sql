/*
Lylah Majernik
Programming 2 Final
Submitted 5/7/2025
*/

CREATE TABLE IF NOT EXISTS TRAINER
                    (ID         INTEGER      PRIMARY KEY,
                     Name       TEXT         NOT NULL UNIQUE,
                     Email      TEXT,
                     Phone      INTEGER,
                     Team       INTEGER      DEFAULT NULL)STRICT
                                                