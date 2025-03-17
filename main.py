import auth, physics_calculator, source_finder, sys, db_utils

print("Welcome to student tools by Dashcorp!")
authorized=auth.auth()
if authorized == False:
    print("Access denied")
    sys.exit("Exiting program")
print("Welcome to Dashcorp!")