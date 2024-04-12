#It is a block of code& it only runs when it is called.
#"Write once & call anywhere...."

#Syntax:-
# def Name(parameter):
#     return 0
# Name(Arguments)

#From a function's perspective:
# 1. A parameter is the variable listed inside the parentheses in the function definition.

# 2. An argument is the value that is sent to the function when it is called.


# def full_name(fname, lname):
#     return fname + lname

# print(full_name('shashank', 'kotla'))


#Arbitrary Arguments - (*args):-
# def args(*args1):
#     return sum(args1)
# print(args(1, 3, 4,5))

#Keyword Arguments :- send arguments with the key = value syntax.
# def keyword(fname, lname):
#     return fname + lname
# print(keyword(lname='Kotla', fname="Shashank"))


#Arbitary Keyword Arguments, **kwargs:-
# ----------------------------------
#1. It will receive a dictionary of arguments
#2. If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#---------------------------------------
# def arbitrary_keyword(**name):
#     print(name)
# arbitrary_keyword(fname='shashank', lname="Kotla", mname= None)

#Default parameter value:-
# def fun(country = "United states of America"):
#     return country
# print(fun("INDIA"))
# print(fun())

#Passing a list as an Argument:-
# def my_fun(test):
#     for x in test:
#         print(x)
# test = ['one', 'two', 'three']
# my_fun(test)


#Return values
# def cal(x):
#     return 5 * x
# print(cal(9))

#Pass Statement - it's like i addon content next time.
# def fun():
#     pass



#Note: function can have ONLY positional arguments, or ONLY keyword arguments.
#Positional-only Arguments

# def fun(x , /):
#     print(x)
# fun(4)

# def fun(x):
#     print(x)
# fun(x=6)
# -------------------------
# Positional arguments: Passed based on the position/order in the function definition.
# Keyword arguments: Explicitly mention the parameter name along with the value.
# ----------------------------
#Keyword-Only Arguments
# def my_function(*, x):
#     print(x)
# my_function(x=5)
# my_function(5) #TypeError: my_function() takes 0 positional arguments but 1 was given


#Combine Positional-only & keyword-only
# Note:-Any argument before the / , are positional-only, and any argument after the *, are keyword-only.


# def my_function(a, b, /, *, c,d):
#     print(a + b + c + d)
# my_function(5, 6, d=7, c=9)

#Recursion -a defined function can call itself.

# def tri_recursion(k):
#     if(k>0):
#         result = k + tri_recursion(k-1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("Recursion Example Results")
# tri_recursion(6)



