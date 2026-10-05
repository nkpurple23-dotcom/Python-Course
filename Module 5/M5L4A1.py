class myClass:
    __privateVar=27
    def __privMeth(self):
        print("Hello.")
    def hello(self):
        print(myClass.__privateVar)
foo=myClass()
print(foo)
foo.hello()
foo.__privMeth()