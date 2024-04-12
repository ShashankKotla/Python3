
import os

# file = open("my_details.txt", "x")
# file.close()

# file = open("my_details.txt", "w")
# def details(name, age, email):
#     return f"My name is: {name} and age is: {age}. Here is my {email}!"
# file.write(details('shashank', '21', 'test@mail.com'))
# file.close()

# file = open("my_details.txt", "r")
# print(file.read())

# file = open("my_deatils", "w")
# def details():
#     name =input("enter you name:")
#     age = input("Enter your age:")

#     return f"my name is: {name} & my age is {age}"
# file.write(details())
# file.close()

# file = open("my_details.txt", "r")
# print(file.read())
# file.close()

# #delete
# if os.path.exists('my_details.txt'):
#     os.remove('my_details.txt')
#     print("File Removed!")
# else:
#     print("process have not happened!")
    
# file = open("text.txt", "x")
# file.close()

# def details():
#     name = input("Name: ")
#     age = input("Age: ")
#     return name + age




class Info:
    global name, age
    name = input("name: ")
    age = input("age: ")

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        # pass

    def full_name(self):
        print(self.name , self.age)

test = Info(name, age)
test.full_name()





