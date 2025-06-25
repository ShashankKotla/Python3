"""
🔹 7. Error Handling with try & except
🧠 Why Use It?
Errors like:

File not found

Division by zero

Wrong data types

Accessing undefined variables

...can crash your program 💥 unless you handle them properly using try & except.

✅ Basic Structure
python
Copy code
try:
    # risky code here
    x = 1 / 0
except:
    # runs if error happens
    print("Something went wrong!")
🧾 Output:

nginx
Copy code
Something went wrong!
🔍 Types of Errors You Can Catch
You can catch specific errors too (which is best practice):

Error	               Cause
ZeroDivisionError	Dividing by 0
FileNotFoundError	Opening a missing file
TypeError            Wrong data type used
ValueError	        Bad value (e.g., converting 'abc' to int)
NameError	        Variable not defined
"""


# try:
#     num = int('abc')
# except ValueError:
#     print("Please enter a valid number.")

"""
 try:
    print("Try block running")
except:
    print("Error happened")
else:
    print("No error! This runs.")
finally:
    print("This always runs.")

"""

print("Please enter you inputs:")
input1 = int(input("input1: "))
input2 = int(input("input2: "))

try:
    div = input1/input2
    print(div)
except ValueError:
    print("Please enter numbers only")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("No error! This runs.")
finally:
    print("Every thing went smooth!")