import os
import psycopg2 as db


class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database=os.getenv("DATABASE"),
            host=os.getenv("DATA_HOST"),
            user=os.getenv("DATA_USER"),
            password=os.getenv("DATA_PASSWORD")
        )
        cursor = database.cursor()
        cursor.execute(query)
        if query_type == "insert":
            database.commit()
            return "Successful inserted"

        if query_type == "select":
            return cursor.fetchall()