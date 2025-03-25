class Bank:
    def __init__(self, name, ammount, pin):
        self.name=name
        self.ammount=ammount
        self.pin=pin
    
    def get_name(self):
        print(self.name)
    
    def set_name(self,new_name):
        self.name = new_name
        print(self.name)
    
    def showBank(self):
        print("Hello {}, you currently have ${} in your account. Set your pin here ____. {}       ".format(self.name,self.ammount,self.pin))
    
P1=Bank("Jace Williams", "2.6M", "4285")

P1.showBank()
