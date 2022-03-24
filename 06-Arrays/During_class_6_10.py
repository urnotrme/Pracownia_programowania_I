def array2str(array):
    for i in array:
        a=str(i)
        b=" ".join(a)
    print("Array:", b)

def suma(array):
    suma=0
    for i in range(0, len(array)):
        suma+=array[i]
    print("Sum of values:", suma)
    
    
array=[4, 3, 7, 1, 3]
array2str(array)
suma(array)