n=[12, 6, 4, 9, 10]
def star(n):
    st="*"
    for i in range(0, len(n)):
        print(f"{n[i]}: {st*n[i]}")

star(n)
