list = ["Once upon a time", "Bad genius", "Sky castle",
        "Harry Potter", "1+1"]

with open("films.txt", 'a')as f:
    for i in list:
        print(i, file=f)