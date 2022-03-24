import random
with open("randint.txt", "a") as f:
    for i in range(1,51):
        print(random.randint(100,999), file=f)