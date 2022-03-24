names=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
n=''
for i in range(0, len(names)):
    n+=names[i]+" "
print("Names:", n)
mx=""
for i in range(0, len(names)):
    if len(names[i])>len(mx):
        mx=names[i]
print("Longest name:", mx)
