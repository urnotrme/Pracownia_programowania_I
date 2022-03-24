ar=[2, 3, 2, 5, 8, 1, 9, 8]
s=''
for i in range(0, len(ar)):
    s+=str(ar[i])+" "
print("Array: ", s)
d=''
for i in range(0, len(ar)):
    c=True
    for x in range(0, len(ar)):
        if ar[i]==ar[x]:
            c=False
    if c==True:
        d+=str(ar[x])+' '
print("Unique elements: ", d)
