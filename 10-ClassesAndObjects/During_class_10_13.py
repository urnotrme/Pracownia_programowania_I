class TV():
    def __init__(self):
        self.is_on = False
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on:
            print("TV is on")
        else:
            print("TV is off")
        
    def channels_list(self, channels_list):
        self.channels_list = channels_list
        
    def set_channels(self, channels_list):
        s=''
        for x in range(len(channels_list)):
            s+=f"\n{x+1}. {channels_list[x]}"
        self.channels_list = s           
        
    def show_channels(self):
        print("Channel list:", self.channels_list)
               
        
            
t1 = TV()
t1.show_status()
t1.turn_on()
t1.show_status()
t1.channels_list('No channels list')
t1.show_channels()
t1.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
t1.show_channels()
t1.show_status()
t1.turn_off()
t1.show_status()
