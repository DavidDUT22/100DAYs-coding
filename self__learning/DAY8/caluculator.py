
#SIMPLE CALCULATOR
num1 = float(input("please enter 1st number: "))
operator =input("Enter an operator(+ - * / %): ")
num2 = float(input("please enter 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} {operator} {num2} = {result }")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} {operator} {num2} = {result }")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} {operator} {num2} = {result }")
elif operator == "/":
    result = num1 + num2
    print(f"{num1} {operator} {num2} = {result }")
elif operator == "%":
    result = num1 % num2 
    print(f"{num1} {operator} {num2} = {result }")
else:
    print("invalid input")
    


   
 