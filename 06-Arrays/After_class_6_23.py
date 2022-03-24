def median(array):
    a=0
    if len(array)%2==0:
        a=int(len(array)/2)-1
        b=int((len(array)/2))
        c=(array[a]+array[b])/2
        print(c)
    else:
        a=int((len(array)/2))
        print(array[a])

median([1,0,9,8,4,6])
median([6,8,3,1,0,5,7])
