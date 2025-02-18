# Decorators uses the "@decorator_function" syntax and essentially functions that take another function as an argument and return a new function.


def my_decotator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

#Apply the decorator using '@'
@my_decotator
def say_hello():
    print("say_hello")

say_hello()


# Link of doc: https://medium.com/@chanataranjeet/understanding-python-decorators-a-concise-guide-eac4a19eb982
# Explanation:
# 1. my_decotator function that takes another function as an argument
# 2. Wrapper is a nested function within my_decotator that adds extra functionality before and after the original function is called.
# 3. @my_decotator is used above the say_hello() function declaration, indicating that say_hello will be passed to my_decorator as an argument.
# 4. When say_hello() is called, it actually executes the wrapper function created by the decorator. This allows for the additional behaviour to added before and after the original say_hello function execution.
    
# Conclusion:
# Decorators are a versatile tool in python that enable you to modify the behaviour of functions without changing their actual code. they are widely used in frameworks like flask and django for thaks such as authentication, logging and more . 
