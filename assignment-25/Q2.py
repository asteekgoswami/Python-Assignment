# Write a python script to update the above Profile class with encapsulation

class Profile:
    def __init__(self,name,email,age) -> None:
        self.name=name
        self.age=age
        self.email=email
    
    def show(self):
        print(self.name)
        print(self.email)
        print(self.age)
        
    

obj1=Profile('Asteek','asteekgoswami650@gmail.com',20)
obj1.show()