first=input("Enter first num: ")
operator= input("Enter a operator(+,-,*,/) : ")
second= input("Enter second num: ")
first= int(first)
second= int(second)
if operator=="+":
    print(first + second)
elif operator=="-":
    print(first - second)
elif operator=="*":
    print(first * second)
elif operator=="/":
    print(first / second)
else:
    print("Invalid operator")