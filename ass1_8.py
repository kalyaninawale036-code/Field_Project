def factorial_loop(n):
    """
    Calculates the factorial of a non-negative integer using a loop.

    Args:
        n: The non-negative integer for which to calculate the factorial.

    Returns:
        The factorial of n. Returns 1 if n is 0 or 1.
        Returns an error message if n is negative.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

try:
    number = int(input("Enter a non-negative integer: "))
    fact = factorial_loop(number)
    if isinstance(fact, str):
        print(fact)
    else:
        print(f"The factorial of {number} is {fact}")
except ValueError:
    print("Invalid input. Please enter an integer.")