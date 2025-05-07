/*
Lylah Majernik
Programming 2 Final
Submitted 5/7/2025
*/


CREATE TABLE IF NOT EXISTS MEMBERSHIP
                    (PokemonID    INTEGER,
                     TeamID       INTEGER,
                     FOREIGN KEY(PokemonID) REFERENCES POKEMON(ID),
                     FOREIGN KEY(TeamID) REFERENCES TEAM(ID))STRICT
