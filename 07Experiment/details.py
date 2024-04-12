class details:
    
    def __init__(self, name, age, email) -> None:
        name = input("Name: ")
        age = input("age: ")
        email = input("Email: ")
        self.name = name
        self.age = age
        self.email = email

    def info(self):
        return f"My name is: {self.name}, age: {self.age} and my email is: {self.email}"
    
        

thing = details('shashank', '21', 'shashank@mail.com')
print(thing.info())


file = open('details.txt', 'w')
file.write(thing.info())
file.close()

file = open("details.txt", "r")
print(file.read())