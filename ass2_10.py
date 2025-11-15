# Get the side length from the user
try:
    side = float(input("Enter the side length of the square: "))
except ValueError:
    print("Invalid input. Please enter a numerical value for the side.")
else:
    # Check if the side is non-negative
    if side < 0:
        print("The side length cannot be negative.")
    else:
        # Calculate the area and perimeter
        area = side * side
        perimeter = 4 * side

        # Display the results
        print(f"The area of the square is: {area}")
        print(f"The perimeter of the square is: {perimeter}")