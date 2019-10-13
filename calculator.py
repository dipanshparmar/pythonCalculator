print("'Copyright 2019 Anshu'")
def callme():
    while True:
        operator = str(input("Enter your operator(+, -, *, /, %) or type 'quit' to exit: "))
        if operator == '+':
            addnums()
        elif operator == '-':
            minusnums()
        elif operator == '*':
            multiplynums()
        elif operator == '/':
            dividenums()
        elif operator == '%':
            modulusnums()
        elif operator == "quit":
            break
        else:
            print("Invalid operator selected")
            callme()
def addnums():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "+", num2, "=", num1 + num2)
    except:
        print("Invalid value entered")
        addnums()
def minusnums():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "-", num2, "=", num1 - num2)
    except:
        print("Invalid value entered")
        minusnums()
def multiplynums():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "*", num2, "=", num1 * num2)
    except:
        print("Invalid value entered")
        multiplynums()
def dividenums():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "/", num2, "=", num1 / num2)
    except:
        print("Invalid value entered")
        dividenums()
def modulusnums():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "%", num2, "=", num1 / num2)
    except:
        print("Invalid value enterd")
        modulusnums()
try:
    callme()
except:
    print("Invalid input entered")
    callme()