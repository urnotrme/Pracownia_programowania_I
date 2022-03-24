class Contact_list():
    def __init__(self):
        self.contact = []
    def add(self, element):
        self.contact.append(element)
    def display(self):
        for self.i in self.contact:
           print(self.i.name.ljust(10), self.i.email.ljust(10), self.i.telephone) 
            
            
        