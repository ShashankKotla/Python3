#str can be '' or "" & displayed by print() or by assign, var

# a =  """  """ -> Multiline string
# """ """ -> It will be comment. If we don't assing to var
#str are array's, we can access them indexing, starts from 0 
# & length starts from 1

# x = "This is a string"
# print(len(x))
# print(x[0])


# Loop
# for x1 in x:
#     print(x1, end=',')

#check - string

# print("is" in x)

# if "is" in x:
#     print("Yes it is present.")
# else:
#     print("No it is not present.")

#check if not
# print("hello" not in x)

# if "hello" not in x:
#     print("true")

#slicing
# x = "This is a string"
# print(x[0])
# print(x[0:])
# print(x[3:])
# print(x[:5])

#-ve indexing
# print(x[4:-1])
# print(x[:-1])

# Modify strings

a = "Hello World"
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.strip())
# print(a.startswith('H'))
# print(a.endswith('d'))

# print(a.replace('H', "J"))

# splits the string into substrings if it finds instances of the separator
# print(a.split()) 

# print(a.count('o'))


# concatenation
# a = "Hello"
# b = "world"
# c = a + b
# print(c)

# d = a + " " + b #to add space b/w words
# print(d)


#Format
# age = 1991
# txt = "I'm Python, i was released in {}"
# print(txt.format(age))

# name = 'gvanrossume'
# age = 1991
# version = 3
# txt = "I'm Python, i was released in {1} & developed by {0} right now the version is Python{2}"
# print(txt.format(name,age, version))

# name = "shashank"
# print(f'name is {name}')



#escape characters:- \', \\, \n , \r, \t, \b, \f, \ooo, \xhh

# txt = "This is \"Python3\""
# txt = "This is \' single quote"
# txt = "This is \n single quote"
# txt = "This is\tsingle quote"
# txt = "This is \bsingle quote"
# txt = "This is \f single quote" #from feed.
# o/p:-
# This is 
#          single quote

# txt = "\110\145\154\154\157"
# txt = "\x48\x65\x6c\x6c\x6f"


#Methods
# txt = "This is string"



# print(txt.casefold()) #upper to lower
# print(txt.center(50)) #space 50
# print(txt.count('is'))

txt = "String"
# print(txt.isalnum())
# print(txt.isalpha())
# print(txt.isascii())
# print(txt.isdecimal())
# print(txt.isdigit())
# print(txt.isidentifier())
#  valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
# print(txt.islower())
# print(txt.isupper())
# print(txt.isprintable())
# print(txt.swapcase())

# print(txt.index('r'))
# print(txt.isspace())
# print(txt.istitle())


# mytuple = ("John", "Peter", "vicky")
# x = "#".join(mytuple)
# print(x)

# my_dict = {"name":"John", "country":"Norway"}
# my_sep = "Test"
# x = my_sep.join(my_dict)
# print(x)
# #Note: When using a dictionary as an iterable, the returned values are the keys, not the values.


# mydict = {83: 80}
# If you use a dictionary, you must use ascii codes instead of characters.
# txt = "Hello Sam"
# print(txt.translate(mydict))

# txt = "Hello Sam!"
# mytable = str.maketrans("S", "p") #method to create a mapping table.
# print(txt.translate(mytable))

# txt = "Hi sam"
# x = "msa"
# y = "ejo"
# mytable = str.maketrans(x, y)
# print(txt.translate(mytable))



# txt = "This will be a string"
# print(txt.partition("be"))

val = "50"
va = val.zfill(10)
print(va)

