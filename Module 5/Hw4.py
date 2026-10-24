class Account:
    def __init__(self,owner,pin):
        self.__pin=pin
        self.owner=owner
    def show_pin_status(self):
        print("Account Owner:",self.owner)
        print("Pin stored inside class.")
    def set_pin(self,new_pin):
        if len(new_pin)==4:
            self.__pin=new_pin
            print("Pin updated.")
        else:
            print("Access Denied")
    def check_pin(self,entered_pin):
        if entered_pin==self.__pin:
            print("Access Granted")
        else:
            print("Access Denied")
    def __str__(self):
        return f"Account holder: {self.owner}"
my_account=Account("Nikitha", "1853")
print(my_account)
my_account.show_pin_status()
my_account.__pin="1373"
my_account.check_pin("1373")
my_account.check_pin("1853")
my_account.set_pin("1373")
my_account.check_pin("1373")