from main import Database


def table():
    users_table = f"""
        CREATE TABLE users(
        users_id SERIAL PRIMARY KEY,
        first_name VARCHAR(30),
        last_name VARCHAR(40),
        username VARCHAR(50),
        chat_id VARCHAR(20),
        create_date TIMESTAMP DEFAULT now());
    """

    prem_table = f"""
        CREATE TABLE premyera(
        premyera_id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        continue_prem VARCHAR(40),
        create_country VARCHAR(30),
        photo_url VARCHAR(200),
        create_date DATE,
        join_bot_date TIMESTAMP DEFAULT now());
    """


    movie_table = f"""
        CREATE TABLE movie(
        movie_id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        continue_prem VARCHAR(40),
        create_country VARCHAR(30),
        photo_url VARCHAR(200),
        create_date DATE,
        join_bot_date TIMESTAMP DEFAULT now());
    """


    cartoon_table = f"""
        CREATE TABLE cartoon(
        cartoon_id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        continue_prem VARCHAR(40),
        create_country VARCHAR(30),
        photo_url VARCHAR(200),
        create_date DATE,
        join_bot_date TIMESTAMP DEFAULT now());
    """


    serial_table = f"""
        CREATE TABLE serial(
        serila_id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        continue_prem VARCHAR(40),
        serial_part SMALLINT,
        create_country VARCHAR(30),
        photo_url VARCHAR(200),
        create_date DATE,
        join_bot_date TIMESTAMP DEFAULT now());
    """

    data = {
        "users_table": users_table,
        "prem_table": prem_table,
        "movie_table": movie_table,
        "cartoon_table": cartoon_table,
        "serial_table": serial_table
    }

    for i in data:
        print(f"{i} - {Database.connect(data[i], "create")}")


if __name__ == '__main__':
    table()