a=[5.7, 8.4, 56.9, 25.1, 1.8, 3.5, 101.1]
n=float(input())
s=''
for i in range(0, len(a)):
    if a[i]>n:
        s+=str(a[i])+" "
print(s)        
