<<<<<<< HEAD
# Calculator...

import math

def add(a,b):
    return round(a + b, 4)
    
def sub(a,b):
    return round(a - b,4)
    
def mult(a,b):
    return round(a*b,4)
    
def div(a,b):
    if b == 0:
        return "Cannot divide by Zero"
    return round(a/b,4)

def power(a,b):
    return round(pow(a,b),4)

def squareroot(a):
    if a < 0:
        return None
    return round(math.sqrt(a),4)


def save_history(history):
    with open('history.txt','a') as f:
        for item in history:
            f.write(item + '\n')
    print("History saved !!")

history = []


all_operations = {
    'add': add,
    'sub':sub,
    'mult':mult,
    'div':div,
    'pow':power
}


try:
    while True:
        operation = input("Operation(exit/add/sub/mult/div/pow/squareroot/history/save) : ").strip().lower()

        # Exit from the calculator..
        if operation == 'exit':
            print("Goodbye!!")
            break

        # History...
        elif operation == 'history':
            if not history:
                print("No History found!! please add")
            else:
                for i,item in enumerate(history,1):
                    print(f'{i}){item}')

        # Save...
        elif operation == 'save':
            save_history(history)



        # Squareroot...
        elif operation == 'squareroot':
            a = float(input("Enter number : "))
            result = squareroot(a)

            if result is None:
                print("Error: square root of negative number is not defined")

            else:
                print(result)
                history.append(f"squareroot of {a} is {result}")


        # All operations (add, sub, mult, div, pow)...
        elif operatiol_operations:

            a = float(input("Enter first number : "))
            b = float(input("Enter second number : "))

            result = all_operations[operation](a,b)
            print(result)
            history.append(f"{operation}({a}, {b}) = {result}")

        else:
            print("Unknown operation .\nplease try again!!")

except Exception as e:
=======
# Calculator...

import math

def add(a,b):
    return round(a + b, 4)
    
def sub(a,b):
    return round(a - b,4)
    
def mult(a,b):
    return round(a*b,4)
    
def div(a,b):
    if b == 0:
        return "Cannot divide by Zero"
    return round(a/b,4)

def power(a,b):
    return round(pow(a,b),4)

def squareroot(a):
    if a < 0:
        return None
    return round(math.sqrt(a),4)


def save_history(history):
    with open('history.txt','a') as f:
        for item in history:
            f.write(item + '\n')
    print("History saved !!")

history = []


all_operations = {
    'add': add,
    'sub':sub,
    'mult':mult,
    'div':div,
    'pow':power
}


try:
    while True:
        operation = input("Operation(exit/add/sub/mult/div/pow/squareroot/history/save) : ").strip().lower()

        # Exit from the calculator..
        if operation == 'exit':
            print("Goodbye!!")
            break

        # History...
        elif operation == 'history':
            if not history:
                print("No History found!! please add")
            else:
                for i,item in enumerate(history,1):
                    print(f'{i}){item}')

        # Save...
        elif operation == 'save':
            save_history(history)



        # Squareroot...
        elif operation == 'squareroot':
            a = float(input("Enter number : "))
            result = squareroot(a)

            if result is None:
                print("Error: square root of negative number is not defined")

            else:
                print(result)
                history.append(f"squareroot of {a} is {result}")


        # All operations (add, sub, mult, div, pow)...
        elif operation in all_operations:

            a = float(input("Enter first number : "))
            b = float(input("Enter second number : "))

            result = all_operations[operation](a,b)
            print(result)
            history.append(f"{operation}({a}, {b}) = {result}")

        else:
            print("Unknown operation .\nplease try again!!")

except Exception as e:
>>>>>>> 0a61c618453bd62d2d0ff9aec6433c8fa8e65d3e
    print("Error Occured : ",e)