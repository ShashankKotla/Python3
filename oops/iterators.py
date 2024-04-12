#An iterator is an object that contains a countable number of values.
# "An iterator is an object that can be iterated upon", meaning that you can traverse through all the values.
#Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
#Lists, tuples, dictionaries, and sets are all iterable objects. They are 'iterable containers' which you can get an iterator from.

# text = ('apple', 'banana', 'cherry')
# text = 'time' #even str is an iterable object.
# my_text = iter(text)

# print(next(my_text))
# print(next(my_text))
# print(next(my_text))

# for i in text:
#     print(i)


#Note:- Sure! Imagine you have a box, and you want to do things with what's inside the box. The word "self" is like saying "this box" or "the box we're working with right now." So, when you say "self.name," it means "the name inside this box." It helps us work with the specific box (or object) we're dealing with at the moment.


# class MyNumbers:
#     def __iter__(self):
#         self.a=1
#         return self # it returns self, indicating that this object itself is an iterator.
#     def __next__(self):
#         s = self.a
#         self.a += 1
#         return s

# myclass = MyNumbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = iter(MyNumbers())
# # myiter = iter(myclass)

# for x in myclass:
#   print(x, end=',')



# class Numbers:

#     def __iter__(self):
#         self.num = 1
#         return self
    
#     def __next__(self):
#         if self.num <=9:
#             x = self.num
#             self.num += 1
#             return x
# value = iter(Numbers())
# print(next(value))
# print(next(value))
# print(next(value))

