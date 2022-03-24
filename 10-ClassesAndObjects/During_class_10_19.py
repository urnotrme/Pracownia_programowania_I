class Statistics():
    def __init__(self, arr=[]):
        self.arr = arr
        
    def pop(self, pop):
        self.arr.append(pop)
        
    def sep(self):
        self.s=''
        for self.i in range(0, len(self.arr)):
            self.s+=str(self.arr[self.i])+" "
        return self.s
        
    def maxi(self):
        self.maxm = max(self.arr)
        print(self.maxm)
        
    def mini(self):
        self.minm = min(self.arr)
        print(self.minm)
        
    def mean(self):
        self.meanm = sum(self.arr)/len(self.arr)
        print(self.meanm)
        
    def median(self):
        self.a=0
        if len(self.arr)%2==0:
            self.a=int(len(self.arr)/2)-1
            self.b=int((len(self.arr)/2))
            self.c=(self.arr[self.a]+self.arr[self.b])/2
            print(self.c)
        else:
            self.a=int((len(self.arr)/2))
            print(self.arr[self.a])
        
st=Statistics([34, 45, 6, 23, 74, 80])
st.pop(50)
print(st.sep())
st.maxi()
st.mini()
st.mean()
st.median()

