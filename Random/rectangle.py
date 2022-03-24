a=int(input("Enter the width of the rectangle: "))
b=int(input("Enter the height side of the rectangle: "))

print("*"*a)
for i in range(b-2):
    print("*", " "*(a-2), "*", sep='')
print("*"*a)
