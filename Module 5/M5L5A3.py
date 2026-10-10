class India:
    def capital(self):
        print("India's capital is New Delhi.")
    def language(self):
        print("India has 22 official languages.")
    def type(self):
        print("India is a developing country.")
class USA:
    def capital(self):
            print("USA's capital is Wasington D.C.")
    def language(self):
        print("USA's official language is English.")
    def type(self):
        print("USA is a developed country.")
obj_ind=India()
obj_usa=USA()
for i in (obj_ind,obj_usa):
    i.capital()
    i.language()
    i.type()