
""" 

📦 Why this matters:
Each mode controls how a file is accessed. Using the wrong one can delete data or cause errors — so you must know them well.
✅ Mode Cheat Sheet
Mode	Full Form	What It Does	Warning
'r'	Read	Opens file for reading	File must exist ❗
'w'	Write	Overwrites file or creates new	Deletes all content ❗
'a'	Append	Adds content to the end	File is created if not exists
'x'	Exclusive Create	Creates a file	❌ Fails if file already exists
"""


# with open("coffee.txt", "w") as f:
#     f.write("☕ Time for a break. \n")

# with open("coffee.txt", "a") as f:
#     f.write("One sip at a time. ☕ \n")

# with open("coffee.txt", "r") as f:
#     print(f.read())


from datetime import datetime

with open("activity.log.txt", "a") as log:
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    person = "- Shashank just ran the logger."
    log.write(date_time + " " + person + "\n")
    

with open("activity.log.txt", "r") as log_read:
    print(log_read.read())