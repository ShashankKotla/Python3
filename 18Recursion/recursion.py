# Recursion
#A function that calls itself to break a problem into smaller subproblems - until a base condition stops the loop.

# Key Rule : Every Recursive function must have a base case to prevent infinite recursion -> which leads to a RecursionError.

# def factorial(n):
#     if n == 0 or n == 1: #base case
#         return 1
#     return n * factorial(n-1) #recursive call


def sum_digits(n):
    if n == 0:
        return 0
    return n%10 + sum_digits(n//10)

n=1234
print(sum_digits(n))

""" 
 2. What does n % 10 + sum_digits(n // 10) mean?
📦 Goal: Break number into digits and add
Let’s take:

python
Copy code
n = 1234
We want: 1 + 2 + 3 + 4 = 10

🧠 Trick to break a number:
n % 10 → gives last digit

n // 10 → removes last digit

Expression	Result
1234 % 10	4
1234 // 10	123

🔁 How recursion works:
python
Copy code
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
Step-by-step for sum_digits(1234):

Copy code
sum_digits(1234)
= 4 + sum_digits(123)
= 4 + 3 + sum_digits(12)
= 4 + 3 + 2 + sum_digits(1)
= 4 + 3 + 2 + 1 + sum_digits(0)
= 4 + 3 + 2 + 1 + 0
= 10
🎯 Final Tip:
Think of recursion like peeling digits right to left:

%10 → current digit

//10 → the rest

And you keep peeling till nothing left (n == 0).


"""


