a=[4,36,12,28,9,44,5]
b=[5,1,36]
s=''
for i in range(0, len(a)):
    c=True
    for x in range(0, len(b)):
        if a[i]==b[x]:
            c=False
    if c==True:
        s+=str(a[i])+' '

print(s)
