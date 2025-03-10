import auth, physics_calculator, source_finder, sys

print("Welcome to student tools by Dashcorp!")
authorized=auth()
if authorized == False:
    print("Access denied")
    sys.exit("Exiting program")
print("Welcome to Dashcorp!")