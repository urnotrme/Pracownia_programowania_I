def occurs(number, array):
    print("Number:", number)
    a=''
    for i in array:
        a+=str(i)
        a+=' '
    print("Array:", a)
    for i in range(0, len(array)):
        if number==array[i]:
            print(f"Result: number {number} appears in the array")
        else:
            print(f"Result: number {number} doesn't appear in the array")

array=[15, 38, 7, 23, 14]
number=int(input())
occurs(number, array)

