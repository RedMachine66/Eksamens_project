import math

def calculate_projectile(start_speed , angle_degrees): 
    g = 9.81  # Gravitational acceleration (m/s²)

    # Convert angle from degrees to radians
    angle = math.radians(angle_degrees)

    # Calculate flight time
    flight_time = (2 * start_speed * math.sin(angle)) / g

    # Calculate maximum height
    max_height = int(start_speed**2 * math.sin(angle)**2) / (2 * g)

    # Calculate range
    range_distance = (start_speed**2 * math.sin(2 * angle)) / g

    # Print results
    print(f"\nFlight time: {flight_time:.2f} seconds")
    print(f"Maximum height: {max_height:.2f} meters")
    print(f"Range: {range_distance:.2f} meters")


def get_input_and_calculate(): 
    #User input and ensure user input i valid 
    while True:
        try:
            v0 = float(input("Enter start speed (m/s): "))
            if v0 <= 0:
                print("speed must be a positive number!")
            break
        except ValueError:
            print("enter a valid number")

    while True:
        try:
            angle = float(input("Enter angle (degrees): "))
            if angle <= 0 or angle >= 180:
                print("angle must be a positive number or a number there is not over 180 degress!")
            else:
                break #exit the loop if input is valid 
        except ValueError:
            print("Enter a numeric number")

    # Call the function
    calculate_projectile(v0, angle)