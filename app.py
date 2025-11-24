# Welcome
print("Welcome to my Python Program!")
# Ask user for numeric input
books = input("How many books did you read today?")
# Basic error handling for non-numeric values
try:
    books = float(books)
except ValueError:
    print("Please enter a valid number.")
    exit()
# Perform Calculation
weekly_books = books * 7
# Display Book Count
print(f"You are on track to read {weekly_books} books this week.")
print(f"Keep up the Good Work!")
