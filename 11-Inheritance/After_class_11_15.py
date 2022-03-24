class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'P({self.x},{self.y})'

    def __eq__(self):
        if self.x == self.y:
            return "The distance between two defined points is 0."
        else:
            return abs(self.y-self.x)
            
p = Point(3, 6)
print(p)
print(p.x == p.y)
