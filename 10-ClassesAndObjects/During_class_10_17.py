import random
class thermometer():
    def __init__(self):
        self.mon = False
    def on(self):
        self.mon=True
        
    def off(self):
        self.mon=False   
        
    def rand_temp(self):
        self.a = random.randrange(3400, 4200, 10)/100
        
    def show(self):
        if self.mon:
            if self.a>37 and self.a<41:
                print(f"Temperature: {self.a}C (fever)")  
            elif self.a>=41:
                print(f"Temperature: {self.a}C (CRITICAL TEMPERATURE!!)")
            else:
                print(f"Temperature: {self.a}C (norm)")
            
t1=thermometer()
t1.on()
t1.rand_temp()
t1.show()
t1.off()
            
        
        
        