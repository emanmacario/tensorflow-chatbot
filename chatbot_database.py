import sqlite3
import json
from datetime import datetime

timeframe = '2015-01'
sql_transaction = []

# Establish connection
connection = sqlite3.connect('{}.db'.format(timeframe))
cursor = connection.cursor()


def create_table():
    """Creates an embedded database"""
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


def format_data(data):
    """Clean up data"""
    data = data.replace("\n", " newlinechar ").replace("\r", " newlinechar ").replace('"', "'")
    return data



def find_parent(parent_id):
    try:
        sql = """SELECT comment FROM parent_reply 
                 WHERE comment_id = '{}' LIMIT 1""".format(parent_id)

        cursor.execute(sql)
        result = cursor.fetchone()

        if result != None:
            return result[0]
        else:
            return False

    except Exception as e:
        print("find_parent", e)
        return False



# Main program
if __name__ == "__main__":
    create_table()
    row_counter = 0
    paired_rows = 0

    with open("D:/Projects/tensorflow-chatbot/RC_2015-01", buffering=1000) as f:
        for row in f:
            print(row)
            row_counter += 1
            row = json.loads(row)
            parent_id = row['parent_id']
            body = format_data(row['body'])
            created_utc = row['created_utc']
            score = row['score']
            subreddit = row['subreddit']