def reverse_number_loop(num):
  """
  Reverses a given integer using a while loop.

  Args:
    num: The integer to be reversed.

  Returns:
    The reversed integer.
  """
  reversed_num = 0
  while num > 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Add the digit to the reversed number
    num //= 10  # Remove the last digit from the original number
  return reversed_num

# Get input from the user
number = int(input("Enter a number to reverse: "))

# Call the function and print the result
reversed_result = reverse_number_loop(number)
print(f"The reversed number is: {reversed_result}")