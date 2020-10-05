class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Welcome {}, he is {} years old.".format(name,age))

class teacher(person):
    def print(self,name,age):
        person.__init__(self,name,age)
        
        
class student(person):
    def print(self,name,age):
        person.__init__(self,name,age)