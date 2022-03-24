def compare(array1, array2):
    a=True
    for i in range(0, len(array1)):
        if len(array1)==len(array2) and array1[i]==array2[i]:
                   a=True
        else:
            a=False
    a1=''
    for i in range(0, len(array1)):
                   a1+=str(array1[i])
                   a1+=" "
    print("Array1:", a1)
    a2=''
    for i in range(0, len(array2)):
                   a2+=str(array2[i])
                   a2+=" "
    print("Array2:", a2)
    if a==True:
                   print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are not the same")

compare(["water","book","sky"], ["water","book","sky"])
compare([True, False], [True, False, True])
compare([5,3,1], [5,3,1])
compare([3,2,1], [3,2])