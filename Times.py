#to print n number times
num=input("Enter the number: ")
num = int(num)
for i in range(11):
    if i == 0:
        continue
    print("Time of " +str(num)+ " x " +str(i)+ " = "+str(num*i)+"")
