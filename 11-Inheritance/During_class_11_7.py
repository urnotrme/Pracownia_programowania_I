class Message():
    def __init__(self):
        self.message = ''   
    def set_message(self,message):
        self.message=message.capitalize()+" Bye."
    
class SMS():
    def __init__(self, ph_num, recipient):
        super().__init__()
        self.ph_num = ph_num
        self.recipient = recipient
    def send(self):
        a = f"Sending SMS...\nFrom:\t{self.ph_num}\nTo:\t{self.recipient}\n{self.message}"
        return a
    
class Email():
    def __init__(self, send_add, rep_add, subject):
        super().__init__()
        self.send_add = send_add
        self.rep_add = rep_add
        self.subject = subject
    
    def send(self):
        a = f"Sending email...\nFrom:\t{self.send_add}\nTo:\t{self.rep_add}\nSubject:\t{self.subject}\n{self.message}"
        return a
    
mes = Message()
mes.set_message("I would like to inform you that our Thursday meeting has been canceled.")
email = Email("nowak@onet.pl", "kowalski@gmail.com", "Meeting on Thursday")
print(email.send())