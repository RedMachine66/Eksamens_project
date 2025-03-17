import db_utils, hashlib, re

# SQLite with python docs: https://docs.python.org/3/library/sqlite3.html
# Python haslib docs: https://docs.python.org/3/library/hashlib.html


DB_PATH = 'dashcorp.db'

def login(con, hashed_user_email):
    print("please enter your password")
    hashed_user_password=auth_hash(input())
    if db_utils.check_password(con, hashed_user_email, hashed_user_password):
        return True
    else:
        print("Incorrect password")
        return False

def auth_create_account(con, hashed_user_email):
    while True:
        print("Enter new password")
        new_password=input()
        if len(new_password) >= 6:
            new_hashed_user_password=auth_hash(new_password)
            print("Enter you telephone number")
            hashed_tlf = auth_hash(input())
            return db_utils.create_user(con, hashed_user_email, new_hashed_user_password, hashed_tlf)
        print("Password must be over 6 characters")

def auth_hash(input):
    encoded_input=input.encode("utf-8")
    hash=hashlib.sha256(encoded_input)
    return hash.hexdigest()

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"
    return re.match(pattern, email) is not None



def auth():
    con=db_utils.connect_to_db(DB_PATH)
    email_input_tries = 0
    while True:
        if email_input_tries >= 3:
            return False
        print("Please enter your email to log-in or sign-up.")
        user_email=input().strip()
        if not is_valid_email(user_email):
            print("Not a valid email")
            continue
        hashed_user_email=auth_hash(user_email)
        if db_utils.email_exists(con, hashed_user_email):
            password_input_tries = 0
            while True:
                if password_input_tries < 3:
                    logged_in=login(con, hashed_user_email)
                    if logged_in:
                        return True
                else:
                    return False
                password_input_tries += 1
        elif email_input_tries < 3:
            print("Your email is not associated with an existing account, do you want to create one? (y/n)")
            should_create_account=input()
            if should_create_account == "y":
                create_account=auth_create_account(con, hashed_user_email)
                if create_account:
                    return True
                else:
                    print("Account creation failed")
                    return False
            email_input_tries += 1