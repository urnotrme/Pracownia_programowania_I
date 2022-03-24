colors=["white", "pink", "purple", "yellow", "orange", "light green"]
with open("colors.txt", 'a')as f:
    for i in colors:
        print(i, file=f)
