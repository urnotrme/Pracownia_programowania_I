class University():

    # object constructor (__init__ method)
    def __init__(self, name):
        # object states/attributes (fields)
        self.name = name  
    # object bahaviors (methods)
    def print_name(self):  
        print(self.name)
        
    def set_name(self, name):
        self.name = name
        
        
u1 = University('UEK')
u1.print_name()
u1.set_name('UJ')
u1.print_name()

