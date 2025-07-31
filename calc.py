num1=float(input("first number: "))
num2=float(input("second number: "))
operation=input("operator: ")

#operation
#sumNumbers
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
#subNumbers
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
#multiplyNumbers
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} ={result}")
#divideNumbers
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Number divided by zero is zero")
else:
    print("Operator does not exist")