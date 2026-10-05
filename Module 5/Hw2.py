class DailyMessage:
    def __init__(self):
        self.message=""
    def get_message(self):
        self.message=input("Enter a message: ")
    def print_message(self):
        print(self.message.upper())
daily_text=DailyMessage()
daily_text.get_message()
daily_text.print_message()
class HelperSession:
    def __init__(self):
        print("Daily Data Helper session created")
    def __del__(self):
        print("Daily Data Helper session ended")
    def create_session(self):
        session=HelperSession()
        return session
session_obj=HelperSession().create_session()
class PairFinder:
    def find_pair(self,numbers,target):
        lookup={}
        for index,number in enumerate(numbers):
            needed=target-number
            if needed in lookup:
                return (lookup[needed],number)
            lookup[number]=index
        return None
numbers=[10,20,30,40,50,60,70,80,90,100]
target_value=int(input("Enter target sum to search for: "))
result=PairFinder().find_pair(numbers,target_value)
if result is not None:
    print("index1=%d,index2=%d"%result)
else:
    print("No matching pair")