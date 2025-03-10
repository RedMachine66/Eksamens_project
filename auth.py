import db_utils, hashlib

# SQLite with python docs: https://docs.python.org/3/library/sqlite3.html
# Python haslib docs: https://docs.python.org/3/library/hashlib.html

db_path = 'dashcorp.db'

def auth():
    while True:
        print("Please enter your email to log-in or sign-up.")
        user_email=input()
        con=connect_to_db(db_path)
        if email_exists(con, user_email):
            while True:
                logged_in=auth_login(con, user_email)
                if logged_in:
                    return True
        else:
            print("Your email is not associated with an existing account, do you want to create one? (y/n)")
            user_create_account=input()
            if user_create_account == "y":
                account_created=auth_create_user(con, user_email)
                if account_created:
                    return True



def auth_login(con, user_email):
    print("please enter your password")
    user_password=input()
    if check_password(con, user_email, user_password):
        return True
    else:
        print("Incorrect password")
        return False

def auth_create_user(con, user_email):
    print("Enter new password")
    new_user_password=input()
    create_user(con, user_email, new_user_password)
    return True