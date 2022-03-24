a=int(input("Enter the amount in PLN: "))
zł5 = int(a/5)
print(f"The amount of PLN {a} in coins:")
a -= zł5*5
zł2 = int(a/2)
a -= zł2*2
zł1 = int(a/1)
print(f"5 zł – {zł5}\n2 zł – {zł2}\n1 zł – {zł1}")

