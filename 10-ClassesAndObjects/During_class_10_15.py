class TV():
    def __init__(self):
        self.vol = 0
        
    def increase(self):
        if self.vol<10:
            self.vol += 1
        
    def decrease(self):
        if self.vol>0:
            self.vol -= 1
        
    def show_status(self):
        print(self.vol)
            
t1 = TV()
t1.show_status()
t1.increase()
t1.show_status()
t1.increase()
t1.show_status()
t1.decrease()
t1.show_status()