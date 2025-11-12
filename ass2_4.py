import math

try:
    radius = float(input("Enter the radius of the circle: "))
except ValueError:
    print("Invalid input. Please enter a numeric value for the radius.")
    exit()

if radius < 0:
    print("The radius cannot be negative. Please enter a positive value.")
else:
    
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius

    print(f"The area of the circle is: {area:.2f}")
    print(f"The circumference of the circle is: {circumference:.2f}")