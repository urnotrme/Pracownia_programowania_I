a=[5,1,9,6,1]
print("Array:", a)
mx=max(a[0],a[1])
secondmax=min(a[0],a[1])
for i in range(2,len(a)):
    if a[i]>mx:
        secondmax=mx
        mx=a[i]
    elif a[i]>secondmax and mx != a[i]:
        secondmax=a[i]
print("Result:", secondmax)
