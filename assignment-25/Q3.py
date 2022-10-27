# Write a python script to update 2nd Question, change email and age to __email and
# __age


class Profile:
    def __init__(self,name,email,age) -> None:
        self.name=name
        self.__age=age
        self.__email=email
    
    def show(self):
        print(self.name)
        print(self.__email)
        print(self.__age)
        
    

obj1=Profile('Asteek','asteekgoswami650@gmail.com',20)

obj1.name='Ram'
obj1.email='shriram@gmail.com'
obj1.age=21

obj1.show()