
# Get user input
num = int(input("Enter a number: "))
age = int(input("Enter your age: "))
month = int(input("Enter a month (1-12): "))
year = int(input("Enter a year: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Check if the number is positive, negative, or zero
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")

# Check if the number is divisible by both 2 and 3 or anyone of them or not divisible by both
if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by both 2 and 3.")
elif num % 2 == 0:
    print(f"{num} is divisible by 2 but not 3.")
elif num % 3 == 0:
    print(f"{num} is divisible by 3 but not 2.")
else:
    print(f"{num} is not divisible by both 2 and 3.")

# Check eligibility to vote
if age >= 18:
    nationality = input("Are you Pakistani? (yes/no): ")
    if nationality.lower() == "yes":
        print("You are eligible to vote.")
    else:
        print("Please obtain a valid ID to vote.")
else:
    print("You are not eligible to vote.")

# Determine age category
if age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 59:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Print number of days in a month
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Month {month} has 31 days.")
elif month == 2:
    print(f"Month {month} has 28 days.")
else:
    print(f"Month {month} has 30 days.")

# Check if a year is a leap year
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
