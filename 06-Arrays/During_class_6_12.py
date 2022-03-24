a=[15, 8, 31, 47, 2, 19]
ex=''
for i in range(0, len(a)):
    ex+=str(a[i])
    ex+=" "
print("existed array:", ex)
re=''
for x in range(len(a)-1, -1, -1):
    re+=str(a[x])
    re+=" "
print("reversed array:", re)