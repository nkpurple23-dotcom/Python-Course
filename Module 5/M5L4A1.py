class myClass:
    __privateVar=27
    def __privMeth(self):
        print("Hello.")
    def hello(self):
        print(myClass.__privateVar)
foo=myClass()
foo.hello()
foo.__privMeth()