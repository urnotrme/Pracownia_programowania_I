import random
class Arrays():

    @staticmethod
    def adding(n, elem):
        array=[]
        for i in range(1, n+1):
            array.append(elem)
        print(array)
            
    @staticmethod
    def randrange(i, m, n):
        array=[]
        a=random.randint(m,n)
        for x in range(1, i+1):
            array.append(a)
        print(array)
        
    @staticmethod
    def deter(array, m, n):
        count=0
        for i in array:
            if i>=m and i<=n:
                count+=1
        print(count)        
    
Arrays.adding(10, 4)
Arrays.randrange(20, -7, 8)
array = [6, 2, 8, -1, 7, 4, -7, -9, -5, -10, 9, 1, -6, 10, 5, 0, -3, -4, -8, -2]
Arrays.deter(array, -1, 1)