
# def decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()
#         print("After the function runs")
#     return wrapper

# @decorator # -> this is the actual wrapper takes the function as argument. mean decorator syntax "@"
# def greet():
#     print("Hello 👋🏻, Shashank!")

# greet()

# Here when greet() passed through the decorator > wrapper> when func() triggers the greet function also triggers and produce o/p.

# Write a decorator that measures execution time of a function:
import time

def time_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Time taken: {end - start:.2f}s")
    return wrapper


@time_decorator
def slow_function():
    time.sleep(5)
    print("Function Complete.")

slow_function()