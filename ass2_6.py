
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a percentage): "))
time = float(input("Enter the time period (in years): "))

simple_interest = (principal * rate * time) / 100

print(f"The Simple Interest is: {simple_interest:.2f}") 