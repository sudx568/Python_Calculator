import math
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return " Zero division error "
    return num1 / num2

def power_value(num1, num2):
    return num1 ** num2

def square_root(num):
    if num < 0:
        return "Error: Negative number"
    return math.sqrt(num)

while True:

    print("\n SCIENTIFIC CALCULATOR ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:

    
        if choice == '1':
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))

            answer = addition(first, second)

            print("Result =", answer)

        
        elif choice == '2':
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))

            answer = subtraction(first, second)

            print("Result =", answer)

        
        elif choice == '3':
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))

            answer = multiplication(first, second)

            print("Result =", answer)

        
        elif choice == '4':
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))

            answer = division(first, second)

            print("Result =", answer)

        
        elif choice == '5':
            first = float(input("Enter base number: "))
            second = float(input("Enter power: "))

            answer = power_value(first, second)

            print("Result =", answer)

        
        elif choice == '6':
            number = float(input("Enter number: "))

            answer = square_root(number)

            print("Result =", answer)

        
        elif choice == '7':
            print("Calculator Closed")
            break

        
        else:
            print("Invalid choice ")

    except ValueError:
        print("Invalid input")