import math

def calculate_projectile(start_speed , angle_degrees): 
    g = 9.81  # Gravitational acceleration (m/s²)

    # Convert angle from degrees to radians
    angle = math.radians(angle_degrees)

    # Calculate flight time
    flight_time = (2 * start_speed * math.sin(angle)) / g

    # Calculate maximum height
    max_height = (start_speed**2 * math.sin(angle)**2) / (2 * g)

    # Calculate range
    range_distance = (start_speed**2 * math.sin(2 * angle)) / g

    # Print results
    print(f"\nFlight time: {flight_time:.2f} seconds")
    print(f"Maximum height: {max_height:.2f} meters")
    print(f"Range: {range_distance:.2f} meters")

# User input
v0 = float(input("Enter start speed (m/s): "))
angle = float(input("Enter angle (degrees): "))

# Call the function
calculate_projectile(v0, angle)
