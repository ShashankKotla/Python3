def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k} : {v}" for k, v in kwargs.items())

        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")

        return func(*args, **kwargs)
    return wrapper

@debug
def say_hello():
    print("Hello!")
@debug
def greet(name, greetings="Hello!"):
    return (f"{greetings}, {name}")

say_hello()
greet('python', greetings="Hola!")


# 1.the code flow start from the below once @debug decorator function 
# 2. for now lets take example of say_hello(), it goes into debug function because decorator is nothing but it should have to pass on through this.
# 3.According to my understanding the function say_hello() became a parameter of debug.
# 4.Next thing will happen is return wrapper, then process of execution of wrapper will start.
# 5. Next thing is return func(), the parameter of func() is connected to the parameter of wrapper so the arg_value and kwargs_value process will happen and later the print () will also executed
# It thing i've given my best understand of code flow gpt. And if i'm correct Just say "YES" that's it  & incase is there any mistakes in my code flow tell me




