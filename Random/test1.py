a = [10,20,30,20,10,50,60,40,80,50,40]
b=[]
c=set()
for x in a:
    if x not in c:
        b.append(x)
        c.add(x)

print(c)
        
