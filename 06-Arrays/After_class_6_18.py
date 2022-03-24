def bubblesort(array):
    for i in range(0, len(array)-1):
        for j in range(0, len(array)-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1]=array[j+1], array[j]
    s=''
    for i in range(len(array)):
        s+=str(array[i])+" "
    print("Sorted array is:", s)


array = [64, 34, 25, 12, 22, 11, 90]
 
bubblesort(array)
