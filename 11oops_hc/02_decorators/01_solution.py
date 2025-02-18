import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end -start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)

#Yes, decorators provide a way to modify or extend the behavior of functions or methods in a reusable and non-invasive manner. They allow you to wrap functions with additional functionality, such as logging, validation, or pre/post-processing of data, without modifying the original function itself. So, in a sense, they control how data is passed and processed. Your understanding is correct.