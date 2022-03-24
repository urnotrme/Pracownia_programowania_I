a=[8, 2, 5, 1, 9]
ar=''
for i in range(0, len(a)):
    ar+=str(a[i])
    ar+=" "
print("Array:", ar)
nd2=''
for x in range(0, len(a)):
    nd2+=str(a[x]**2)
    nd2+=" "
print("2nd power:", nd2)