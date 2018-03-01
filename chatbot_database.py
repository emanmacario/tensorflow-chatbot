import sqlite3
import json
from datetime import datetime

timeframe = '2015-01'
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(timeframe))
cursor = connection.cursor()

def create_table():
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS parent_reply(
            parent_id TEXT PRIMARY KEY,
            comment_id TEXT UNIQUE,
            parent TEXT,
            comment TEXT,
            subreddit TEXT,
            unix INTEGER,
            score INTEGER
        )"""
    )


if __name__ == "__main__":
    create_table()