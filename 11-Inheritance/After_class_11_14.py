import random
class areas():
    @staticmethod
    def circle(r):
        print(f"Circle with radius {r} has area: {3.14*(r**2)}")
            
    @staticmethod
    def rectangle(a, b):
        print(f"Rectangle with sides {a} and {b} has area: {a*b}")
        
    @staticmethod
    def triangle(a, b):
        print(f"Rectangle with base {a} and height {b} has area: {0.5*a*b}")      
    
areas.circle(3)
areas.rectangle(4, 7)
areas.triangle(6, 2)