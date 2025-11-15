# Get the side length from the user
try:
    side = float(input("Enter the side length of the square: "))
    
    # Check if the side length is non-negative
    if side < 0:
        print("Side length cannot be negative. Please enter a positive value.")
    else:
        # Calculate the area and perimeter
        area = side * side
        perimeter = 4 * side
        
        # Display the results
        print(f"The area of the square is: {area:.2f}")
        print(f"The perimeter of the square is: {perimeter:.2f}")

except ValueError:
    print("Invalid input. Please enter a numerical value for the side length.")