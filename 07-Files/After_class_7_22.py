with open("2i3p.txt", "a") as f:
    for i in range(1,11):
        print(f"{i}, {i**2}, {i**3}", file=f)