import os
import psycopg2 as db


class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database="for_bot",
            host="localhost",
            user="postgres",
            password="2609"
        )
        cursor = database.cursor()
        cursor.execute(query)
        data = ["insert", "create"]
        if query_type in data:
            database.commit()
            if query_type == "insert":
                return "Successful inserted"

            elif query_type == "create":
                return "Successful created"

        else:
            return cursor.fetchall()