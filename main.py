import auth, physics_calc, source_finder, sys, db_utils


print("Welcome to student tools by Dashcorp!")
authorized=auth.auth()
if authorized == False:
    print("Access denied")
    sys.exit("Exiting program")
print("Welcome to Dashcorp!")

while True:
    print("Enter 'c' to use the physics calculator, 's' to use the source finder, or 'x' to close the program")
    userinput=input()
    print(userinput)
    if userinput == 'x':
        sys.exit("Exiting program")
    if userinput == 'c':
        while True:
            print("Enter 'b' to go back")
            print("Enter a start speed value to calculate projectile movement")
            userinput_calculator=input()
            if userinput_calculator == 'b':
                break
            physics_calc.get_input_and_calculate()
    if userinput == 's':
        print("The source finder is not implemented yet")
    if userinput not in ('x','c','s'):
        print("Enter a valid input")