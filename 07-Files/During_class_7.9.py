file = open('numbers.txt','r')
a=0
for line in file:
    a+=int(line)
print(a)    
file.close()