import auth, physics_calc, source_finder, sys, pyfiglet, time
from termcolor import colored


banner = pyfiglet.Figlet(font="slant")
print(colored(banner.renderText("Dash Corp"), "blue"))
print(colored("Welcome to student tools by Dashcorp!", attrs=["bold"]))
print("-----")
time.sleep(0.8)

authorized=auth.auth()
if authorized == False:
    print(colored("Access denied", "red"))
    time.sleep(0.4)
    sys.exit("Exiting program")

time.sleep(0.5)

print("-----")
print(colored("Welcome to Dashcorp!", "green"))

while True:
    print("-----")
    print(colored("Dashboard", "blue", attrs=["bold"]))
    print("")
    print("Enter " + colored("'c'", "green") + " to use the physics calculator")
    print("Enter " + colored("'s'", "green") + " to use the source finder")
    print("Enter " + colored("'x'", "green") + " to close the program")
    print("-----")
    user_choice=input()
    if user_choice == 'x':
        sys.exit("Exiting program")

    if user_choice == 'c':
        print("-----")
        print("This calculator helps you calculate the movement of a projectile.")
        time.sleep(0.8)
        print("To use this calculator you need the following information: start speed and angle.")
        time.sleep(0.8)
        print("Press " + colored("'Enter'", "green") + " to proceed. Enter " + colored("'n'", "green") + " to go back")
        init_calc_choice = input()
        if init_calc_choice == 'n':
            continue
        else:
            while True:
                physics_calc.get_input_and_calculate()
                time.sleep(0.8)
                print("-----")
                print("Enter " + colored("'d'", "green") + " to go to dashboard")
                print("Press " + colored("'Enter'", "green") + " to calculate again")
                calc_choice=input()
                if calc_choice == 'd':
                    break

    if user_choice == 's':
        
        while True:
            print("-----")
            print("Which field of study would you like to find sources for?")
            subject = input()
            print("-----")
            print("What would you like to find sources about?")
            search_area = input()
            print("-----")
            print(colored("Finding sources", "blue"))
            print("-----")
            prompt = "subject: " + subject + ", search area: " + search_area
            print(source_finder.get_gemini_response_with_search(prompt))
            print("-----")

            print("Enter " + colored("'d'", "green") + " to go to dashboard")
            print("Press " + colored("'Enter'", "green") + " to find more sources")
            calc_choice=input()
            if calc_choice == 'd':
                break

    if user_choice not in ('x','c','s'):
        print("Enter a valid input")