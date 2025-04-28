import db_utils, hashlib, re
from termcolor import colored

# SQLite with python docs: https://docs.python.org/3/library/sqlite3.html
# Python haslib docs: https://docs.python.org/3/library/hashlib.html


DB_PATH = 'dashcorp.db'
MAX_RETRIES = 3
MINIMUM_PASSWORD_LENGTH = 6

def login(con, hashed_user_email):
    print("Please enter your password")
    hashed_user_password=hash_string(input())
    if db_utils.check_password(con, hashed_user_email, hashed_user_password):
        return True
    else:
        print(colored("Incorrect password", "yellow"))
        return False

def auth_create_account(con, hashed_user_email):
    while True:
        print("Enter new password")
        new_password=input()
        if len(new_password) >= MINIMUM_PASSWORD_LENGTH:
            new_hashed_user_password=hash_string(new_password)
            return db_utils.create_user(con, hashed_user_email, new_hashed_user_password)
        print(colored("Password must be over " + str(MINIMUM_PASSWORD_LENGTH) + " characters", "yellow"))

def hash_string(data):
    encoded_input=data.encode("utf-8")
    hash_obj=hashlib.sha256(encoded_input)
    return hash_obj.hexdigest()

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"
    return re.match(pattern, email) is not None



def auth():
    con=db_utils.connect_to_db(DB_PATH)
    email_input_tries = 0
    while True:
        if email_input_tries >= MAX_RETRIES:
            return False
        print("Please enter your email to log-in or sign-up.")
        user_email=input().strip()
        if not is_valid_email(user_email):
            print(colored("Not a valid email", "yellow"))
            continue
        hashed_user_email=hash_string(user_email)
        if db_utils.email_exists(con, hashed_user_email):
            password_input_tries = 0
            while True:
                if password_input_tries < MAX_RETRIES:
                    logged_in=login(con, hashed_user_email)
                    if logged_in:
                        return True
                else:
                    return False
                password_input_tries += 1
        elif email_input_tries < MAX_RETRIES:
            print("Your email is not associated with an existing account, do you want to create one? (y/n)")
            should_create_account=input()
            if should_create_account == "y":
                create_account=auth_create_account(con, hashed_user_email)
                if create_account:
                    return True
                else:
                    print(colored("Account creation failed", "yellow"))
                    return False
            email_input_tries += 1