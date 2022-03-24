with open("text.txt") as f:
    a=f.read()
    
with open("copy.txt", "a") as c:
    c.write(a)
