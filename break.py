numbers=[1, 2, 3, 4, 5, 6]
i=0
while i < len(numbers) :
    if i==5:
        break
    print(numbers[i])
    i=i+1
print("Another block of  code")
# (u to u)
j=0
while j < len(numbers):
    if j==3:
        continue
    print(numbers[j])
    j=j+1