import sqlite3
from sqlite3 import Error

def create_connection():
    """ create a database connection to a SQLite database """
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')       
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def load_airports(airports):
    """
    Load the airports data into a SQLite database.

    Parameters:
    airports (DataFrame): The airports data.
    """

    conn = create_connection()

    # Load the data into SQLite
    airports.to_sql('airports', conn, if_exists='replace', index=False)

    print("Airports data loaded successfully.")

def load_airlines(airlines):
    """
    Load the airlines data into a SQLite database.

    Parameters:
    airlines (DataFrame): The airlines data.
    """

    conn = create_connection()

    # Load the data into SQLite
    airlines.to_sql('airlines', conn, if_exists='replace', index=False)

    print("Airlines data loaded successfully.")

def load_routes(routes):
    """
    Load the routes data into a SQLite database.

    Parameters:
    routes (DataFrame): The routes data.
    """

    conn = create_connection()

    # Load the data into SQLite
    routes.to_sql('routes', conn, if_exists='replace', index=False)

    print("Routes data loaded successfully.")
