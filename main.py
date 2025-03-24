import auth, physics_calc, source_finder, sys, pyfiglet, time
from rich.console import Console

console = Console()

banner = pyfiglet.Figlet(font='slant')
print(banner.renderText('Dash Corp'))
print("Welcome to student tools by Dashcorp!")
print("-----")
time.sleep(0.8)
authorized=auth.auth()
if authorized == False:
    print("Access denied")
    time.sleep(0.4)
    sys.exit("Exiting program")
time.sleep(0.5)
print("-----")
print("Welcome to Dashcorp!")

while True:
    print("-----")
    print("Enter 'c' to use the physics calculator")
    print("Enter 's' to use the source finder")
    print("Enter 'x' to close the program")
    print("-----")
    userinput=input()
    if userinput == 'x':
        sys.exit("Exiting program")
    if userinput == 'c':
        print("This calculator helps you calculate the movment of a projectile.")
        time.sleep(1)
        while True:
            physics_calc.get_input_and_calculate()
            print("Enter 'd' to go to dashboard")
            print("Press 'Enter' to calculate again")
            user_input_calc=input()
            if user_input_calc == 'd':
                break
    if userinput == 's':
        print("The source finder is not implemented yet")
    if userinput not in ('x','c','s'):
        print("Enter a valid input")