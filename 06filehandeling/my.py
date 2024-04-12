# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)


#READ
# f = open("demofile.txt", "r")
# f = open("/Users/shashankkotla/Desktop/Python#3/oops/oops.txt", "r")
# print(f.read())
# print(f.read(5)) #specify how many characters u want to specify

#read one line, it is quite similar to next()
# print(f.readline()) 
# print(f.readline()) 

# By looping through the lines of the file, you can read the whole file, line by line:
# for x in f:
#     print(x)

# print(f.readline())
# f.close()
# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.


#WRITE
# "a"(append) - will append to the end of the file
# "w"(write) - will overwrite any exisiting content

# f = open("demofile.txt", "a")
# f.write("Now the file has more content")
# f.close

# f = open("demofile.txt", "r")
# print(f.read())

# f = open("demofile.txt", "w")
# f.write("I have deleted the content")
# f.close()

# f = open("demofile.txt", "r")
# print(f.read())

# f = open("demofile2.txt", 'x')
# f.close()


# f = open("demofile2.txt", "w")
# f.write("this is an experiment doc.")
# f.close

# f = open("demofile2.txt", "r")
# print(f.read())


# import os

# if os.path.exists("demofile2.txt"):
#     os.remove("demofile2.txt")
# else:
#     print("This file does not exist")

# os.rmdir("shashank")


