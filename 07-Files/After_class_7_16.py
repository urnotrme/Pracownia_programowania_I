with open("text.txt") as f:
    a=f.readlines()
    b=[]
    for x in range(1,6):
        b=a[5*(x-1):5*x]
        for line in b:
            print(line)
        input()