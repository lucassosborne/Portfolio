# Function

# Function to add two numbers
def add(x, y):
  return x + y

# Function to subtract two numbers
def subtract(x, y):
  return x - y

# Function to multiply two numbers
def multiply(x, y):
  return x * y

# Function to divide two numbers
def divide(x, y):
  return x / y

# Showing user the calc menu
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Taking input from user
while True:
  choice = input("Choose an operation (1/2/3/4) : ")

# Checking if choice is one of the four options

  if choice in ("1", "2", "3", "4"):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue
    if choice == '1':
      print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
      print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
      if num2 == 0:
        print("Error: Cannot divide by zero")
      elif num2 != 0:
        print(num1, "/", num2, "=", divide(num1, num2)) 
  next = input("Want to calculate again? (y/n) : ")
  if next == "n":
    print ("Thank you!")
    break
  elif next == "y":
    continue