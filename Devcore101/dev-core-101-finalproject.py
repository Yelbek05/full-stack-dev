def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "second number cannot be 0 when two numbers are being divided"
    return a / b + a % b

def calculation():
    print("Select the operation")
    print("1. Add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")

    needed = input("Write the needed one: ")
    a, b = map(float, input().split())
    
    if needed == "1":
        print(add(a,b))
    elif needed == "2":
        print(subtract(a,b))
    elif needed == "3":
        print(multiply(a,b))
    elif needed == "4":
        print(divide(a,b))

calculation()

