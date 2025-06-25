"""
6. Generator Functions
🧠 What’s a Generator?
A generator is a function that yields values one by one instead of returning them all at once.

✅ Why Use It?
Regular Function	Generator Function
Returns all values at once using return	Yields values one at a time using yield
Consumes more memory	Super memory efficient
Example: returns full list	Example: yields next item on loop


"""

def square_gen(n):
    for i in range(n):
        yield i * i

gen = square_gen(5)
# print(gen)

for val in gen:
    print(val)

"""
yield pauses the function and remembers state

Continues from where it left off in next loop
"""

def even(e):
    for i in range(e):
        if i % 2 == 0:
            yield i
    else:
        yield "Done!"

get_even = even(11)
for ev in get_even:
    print(ev)