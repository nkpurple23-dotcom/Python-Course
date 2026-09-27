class FamilyMember:
    def __init__(self,eye_color,height):
        self.eye_color=eye_color
        self.height=height
    def show_traits(self):
        print("Eye Color:",self.eye_color)
        print("Height:",self.height)
class Kid(FamilyMember):
    def __init__(self,name,hair_color,eye_color,height):
        self.name=name
        self.hair_color=hair_color
        super().__init__(eye_color,height)
    def show_traits(self):
        print("Name:",self.name)
        print("Hair Color:",self.hair_color)
        super().show_traits()
    def hobby(self,hobby):
        self.hobby=hobby
        print(hobby)
kid=Kid("Mary","black","blue",175)
print(issubclass(Kid,FamilyMember))
kid.show_traits()
kid.hobby("swimming")