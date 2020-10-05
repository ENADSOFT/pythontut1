class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Welcome {}".format(name))
    
    def __str__(self):
        return("name: {}\nage: {}".format(self.name,self.age))
    
    def __del__(self):
        print("memory allocated is deleted")