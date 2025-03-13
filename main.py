import auth, physics_calculator, source_finder, sys, db_utils

con=db_utils.connect_to_db("dashcorp.db")
print(db_utils.email_exists(con, "magnusbakke2011@gmail.com"))

print("Welcome to student tools by Dashcorp!")
authorized=auth.auth()
if authorized == False:
    print("Access denied")
    sys.exit("Exiting program")
print("Welcome to Dashcorp!")