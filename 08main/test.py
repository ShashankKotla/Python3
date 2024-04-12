import test2

def calling():
    test2.version()
    print("taking input from test2")



def main2():
    print('---------------')
    calling()
    print('----------------')
main2()



# Yes, you've got the basic idea right!

# In Python, when you write if __name__ == '__main__':, it's like saying "if this script is being run directly by Python, and not imported from another script, then do something."

# It's like having a main stage where the main performance happens. When Python sees if __name__ == '__main__':, it knows to start the show from here.

# So, it helps to organize your code neatly. Stuff inside if __name__ == '__main__': will only run when you directly run the script, not when you import it into another script. It's like having a backstage area where you prepare things without showing it to the audience until the main show starts.

# It keeps things clean and prevents unnecessary actions when your script is imported elsewhere.