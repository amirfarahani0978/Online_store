from os import name as os_name, system as terminal
from configs import DB_CONNECTION
import psycopg2
HOST = DB_CONNECTION["DBNAME"]
USER = DB_CONNECTION["USER"]
PORT = DB_CONNECTION["PORT"]
PASSWORD = DB_CONNECTION["PASSWORD"]
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
            
        """CREATE TABLE IF NOT EXISTS users(
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            phone VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            national_id VARCHAR(255) NOT NULL,
            age INTEGER NOT NULL,
            pasword VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS orders(
            order_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            order_date VARCHAR(255) NOT NULL,
            FOREIGN KEY (user_id)
                REFERENCES users (user_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS files(
            files_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price INTEGER NOT NULL,
            date DATE NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS order_item(
            order_item_id SERIAL PRIMARY KEY,
            order_id INTEGER NOT NULL,
            file_id INTEGER NOT NULL,
            FOREIGN KEY (order_id)
                REFERENCES orders (order_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (file_id)
                REFERENCES files (files_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS comments(
            comment_id SERIAL PRIMARY KEY,
            file_id INTEGER NOT NULL,
            first_name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL, 
            description VARCHAR(255) NOT NULL,
            FOREIGN KEY (file_id)
                REFERENCES files (files_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
        )

    try:
        conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def clear():
    terminal('cls' if os_name.lower() == 'nt' else 'clear')