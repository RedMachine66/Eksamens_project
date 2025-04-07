# db_utils.py
import sqlite3


# SQLite with python docs: https://docs.python.org/3/library/sqlite3.html


def connect_to_db(db_path):
    """Establish a connection to the SQLite database and return a cursor."""
    con = sqlite3.connect(db_path)  # Connects to the database file
    return con


def close_db_connection(conn):
    if conn: #check if the connection is open
        conn.close() #Close it 
   
def email_exists(conn, email):
    cur = conn.cursor()  # Get a cursor to execute SQL commands
    cur.execute("SELECT 1 FROM users WHERE email = ?", (email,)) # Check if email exists
    return cur.fetchone() is not None  # Returns True if email is found, False otherwise

def check_password(conn, email, password):
    """Check if the provided password matches the stored hash."""
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE email = ?", (email,))
    row = cur.fetchone()  # Fetch the stored password hash
    
    if row:
        stored_password = row[0]  # Extract stored hash
        return stored_password == password  # Compare the stored hash with the input hash
    return False  # Email not found


def create_user(conn, email, password):
    """Create a new user with email a hashed password and phone number."""
    if email_exists(conn, email):  # Check if the email is already registered
        return False

    cur = conn.cursor()
    cur.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()  # Save changes to the database
    return True