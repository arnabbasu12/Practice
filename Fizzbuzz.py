num=input("Enter the num: ")
num=int(num)
for i in range(num):
    if i==0:
        continue
    elif i%3==0 and i%5 ==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)