import gc

# class Demo:
#     def __del__(self):
#         print("Object is being destroyed")
    
# obj = Demo()
# ref1 = obj
# ref2 = obj

# # Delete all refs
# del obj
# del ref1
# del ref2

# gc.collect() #forces garbage collection.


class Shashank:
    def __del__(self):
        print("Mind Cleared")

x = Shashank()
y = x
z=y

del x
del y
del z
