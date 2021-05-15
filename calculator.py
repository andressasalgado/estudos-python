print("My first calculator in python")
action = input("Which operation you wanna do?")

if action == "+" :
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = float(num1) + float(num2)
    print(result)

elif action == "-" :
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = float(num1) - float(num2)
    print(result)

elif action == "/" :
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = float(num1) / float(num2)
    print(result)

elif action == "*" :
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = float(num1) * float(num2)
    print(result)