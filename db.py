import sqlite3
from sqlite3 import Connection, Error
from utils import Message, Room, conv_to_msg

class DB:
    def __init__(self, name:str, path_to_db:str) -> None:
        self.path = f'{path_to_db}/{name}.db'
        self.connection:Connection

    def conn_db(self) -> Connection | None:
        try:
            print("Connecting to database...")
            conn = sqlite3.connect(self.path)
            print("Connection Established!")
            return conn
        except Error as e:
            print("Failed to establish connection.")
            print(f"Error {e} has occured!")
            return None
        
    def insert_msg(self, room_id:str, msg:Message):
        id:int
        if self.select_msgs(room_id) == 0:
            id = 1
        else:
            id = len(self.select_msgs(room_id)) + 1
        qr = f"INSERT INTO {room_id} (id, client, message, datetime) VALUES ({id}, '{msg.client_id}', '{msg.message}', {msg.datetime});"
        cursor = self.connection.cursor()
        try:
            cursor.execute(qr)
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error {e} occured when executing query: {qr}")

    def select_msgs(self, room_id:str) -> list[Message]:
        qr = f"SELECT * FROM {room_id};"
        cursor = self.connection.cursor()
        try:
            cursor.execute(qr)
            self.connection.commit()
            msgs = conv_to_msg(cursor.fetchall())
            return msgs
        except Error as e:
            print(f"Error {e} occured when executing query: {qr}")


    def create_table(self, table:str):
        query:str
        query = f"""CREATE TABLE IF NOT EXISTS {table} (
            id integer primary key,
            client text not null,
            message text not null,
            datetime integer not null
        );"""
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
        except Error as e:
            print(f"Error {e} occured when executing query: {query}")

    def drop_table(self, table:str):
        query = f"DROP TABLE IF EXISTS {table}"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
        except Error as e:
            print(f"Error {e} occured when executing query: {query}")


        
    