def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

print("Select operator: ")
print("add: +")
print("subtract: -")
print("multiply: *")
print("divide: /")

while True:
    operator_input = input("Choose operator: ")

    for choice in ["+", "-", "*", "/"]:
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your first number: "))
        except ValueError:
            print("Please enter a whole number or a float, i.e (2 or 1.2)")

        if choice == "+":
            print("Result: ", add(num1, num2))
        elif choice == "-":
            print("Result: ", subtract(num1, num2))
        elif choice == "*":
            print("Result: ", multiply(num1, num2))
        elif choice == "/":
            print("Result: ", divide(num1, num2))
        break
    else:
        print('Enter a vaild input "+", "-", "*", "/"')
