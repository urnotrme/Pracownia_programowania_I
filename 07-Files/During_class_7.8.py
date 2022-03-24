file = open('countries.txt','r')

k=1
for line in file:
    print(f"{k}. {line}", end="")
    k+=1
file.close()