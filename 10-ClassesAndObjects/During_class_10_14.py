class TV():
    def __init__(self):
        self.is_on = False
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def channel_name(self, channel_name):
        
        
    def channels_list(self, channels_list):
        self.channels_list = channels_list
        
    def show_status(self, channel_no, channel_name):
        if self.is_on:
            print(f"TV is on, {self.channel_no} ({self.channels_list[channel_name-1]})")
        else:
            print("TV is on, no channel")                 
            


t1 = TV()
t1.turn_on()
t1.channels_list(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
t1.show_status('channel 1', 1)
t1.show_status('channel 5', 5)
t1.show_status('channel 7', 7)