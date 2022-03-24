class TV():
    def __init__(self):
        self.is_on = False
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on:
            print("TV is on,", self.channel_no)
        else:
            print("TV is off")
            
    def channel_no(self, channel):
        self.channel_no=channel
        
    def set_channel(self, new_channel_no):
        self.new_channel_no=new_channel_no
        
    def print_channel(self):
        if self.is_on:
            print("TV is on,", self.new_channel_no)
        else:
            print("TV is off")
        
            
t1 = TV()
t1.channel_no("channel 1")
t1.turn_on()
t1.show_status()
t1.set_channel("channel 5")
t1.print_channel()
t1.turn_off()
t1.show_status()