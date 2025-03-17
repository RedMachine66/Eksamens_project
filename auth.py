import db_utils, hashlib

# SQLite with python docs: https://docs.python.org/3/library/sqlite3.html
# Python haslib docs: https://docs.python.org/3/library/hashlib.html


db_path = 'dashcorp.db'

def login(con, hashed_user_email):
    print("please enter your password")
    hashed_user_password=auth_hash(input())
    if db_utils.check_password(con, hashed_user_email, hashed_user_password):
        return True
    else:
        print("Incorrect password")
        return False

def auth_create_account(con, hashed_user_email, tlf):
    print("Enter new password")
    new_hashed_user_password=auth_hash(input())
    print("Enter you telephone number")
    hashed_tlf = auth_hash(input())
    return db_utils.create_user(con, hashed_user_email, new_hashed_user_password, hashed_tlf)

def auth_hash(input):
    encoded_input=input.encode("utf-8")
    hash=hashlib.sha256(encoded_input)
    return hash.hexdigest()



def auth():
    con=db_utils.connect_to_db(db_path)
    print(con)
    while True:
        print("Please enter your email to log-in or sign-up.")
        hashed_user_email=auth_hash(input())
        con=db_utils.connect_to_db(db_path)
        if db_utils.email_exists(con, hashed_user_email):
            while True:
                logged_in=login(con, hashed_user_email)
                if logged_in:
                    return True
        else:
            print("Your email is not associated with an existing account, do you want to create one? (y/n)")
            should_create_account=input()
            if should_create_account == "y":
                create_account=auth_create_account(con, hashed_user_email)
                if create_account:
                    return True
                else:
                    return False