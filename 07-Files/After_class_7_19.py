with open("MeatAndFish.txt") as f:
    a=f.read()
    
with open("GrainsAndBread.txt") as c:
    b=c.read()
    
with open("shoppinglist.txt", "a") as x:
    x.write(a+b)