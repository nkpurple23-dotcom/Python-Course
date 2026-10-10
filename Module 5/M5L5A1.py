from abc import ABC,abstractmethod
class Absclass(ABC):
    def print(self,x):
        print(x)
    @abstractmethod
    def task (self):
        print("Executed")
class text_class(Absclass):
    def task (self):
        print("Done")
test_obj=text_class()
test_obj.task()