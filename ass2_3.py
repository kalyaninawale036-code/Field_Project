def calculate_marks():
    """
    Inputs marks for 5 subjects, calculates and displays total and average marks.
    """
    marks = []
    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i + 1}: "))
                if 0 <= mark <= 100:  # Assuming marks are between 0 and 100
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numerical value for marks.")

    total_marks = sum(marks)
    average_marks = total_marks / len(marks)

    print(f"\nTotal marks: {total_marks:.2f}")
    print(f"Average marks: {average_marks:.2f}")

calculate_marks()