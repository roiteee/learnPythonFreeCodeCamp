num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
op = input("Enter operator")

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid operator")
