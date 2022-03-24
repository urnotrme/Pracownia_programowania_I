a=[4,2,8,4,7,9,5]
s=[]
d=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        s.append(a[i])
    else:
        d.append(a[i])
print(a)
print(s)
print(d)
