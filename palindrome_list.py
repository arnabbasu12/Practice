marks=[]
size=int(input("Enter the size of the list: "))
for i in range(size):
    marks.append(int(input()))
print(marks)
copy_marks=marks.copy()
copy_marks.reverse()
if copy_marks==marks:
    print("Palindrome")
else:
    print("Not palindrome")