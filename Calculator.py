def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x*y

def division(x, y):
    return x/y


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
while True:
    operation = str(input("Enter the operation: "))

    if operation == "+":
        print(f"The Answer is {addition(number1, number2)} ")
        break
    elif operation == "-":
        print(f"The Answer is {subtraction(number1, number2)} ")
        break
    elif operation == "*":
        print(f"The Answer is {multiplication(number1, number2)} ")
        break
    elif operation == "/":
        print(f"The Answer is {division(number1, number2)} ")
        break
    else :
        print("Please enter the correct operation: ")

  
    number3  = input("if you want to continue press a: ")
    if number3 != "a" : 
        False