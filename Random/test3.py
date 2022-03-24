a=input()
try:
    f=open(a)
except:
    print("Nie ma takiego pliku")
    exit()
    
count=0
for i in f:
    if i.startswith("To be"):
        count+=1
        
print(count)