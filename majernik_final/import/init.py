# -*- coding: utf-8 -*-
"""
Lylah Majernik
Programming 2 Final
Submitted 5/7/2025
"""

import sqlite3
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename= '../teambattle.log', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

db = "../teambattle.db"


#initiate tables
try:
    sqlFiles = [
        '../sql/pokemon.sql',
        '../sql/trainer.sql',
        '../sql/team.sql',
        '../sql/membership.sql'
    ]

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    for file_path in sqlFiles:
        with open(file_path, 'r') as file:
            sql = file.read()
            cursor.executescript(sql)
            logger.debug(f"Success - {file_path}")

    conn.commit()
    conn.close()
    logger.info("Database Sucess.")

except Exception as e:
    logger.error(f"Database failed: {e}")
    

