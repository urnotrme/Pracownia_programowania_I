def coins(price):
    zł5 = int(price/5)
    price -= zł5*5
    zł2 = int(price/2)
    price -= zł2*2
    zł1 = int(price/1)
    print(zł1+zł2+zł5)

price=int(input())
coins(price)
