with open("text.txt") as f:
    a=f.read()
    
with open("copylines.txt", "w") as c:
    for i in a:
        c.write(i)

        