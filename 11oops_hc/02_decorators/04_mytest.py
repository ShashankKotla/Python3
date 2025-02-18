import time

def call_with_fullname(func):
    def wrapper(*args, **kwargs):
        print(f"func: {func.__name__} and Full Name: {args} {kwargs}")
        return func(*args, *kwargs)
    return wrapper


@call_with_fullname
def full_name(fname, lname="K"):
    time.sleep(4)
    return fname, lname

print(full_name("Shashank", lname="Kotla"))
