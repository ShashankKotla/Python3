# Regexp, is very stright about the finding in string
# ^ - Beginning
# $ - End
# | logical or (selecting multi parameter)
# [abcd]e => ea, eb...
#[a-g]e
import re #built-in package

# txt = "this is my string"
# x = re.search("^this.*string$", txt)
# if x:
#     print("Present")
# else:
#     print("Not present")


#Regex functions - findall(), search(), spilt(), sub()

#Meta Characters
# txt = "The rain in spain2"
# x = re.findall("[a-m]", txt) #set of char..
# x = re.findall("\d", txt) #escape special char...
# x = re.findall("r..n", txt) #any char...
# x = re.findall("^The", txt) #starts with
# x = re.findall("spain2$", txt)
# if x:
#     print("Yes")
# else:
#     print("Nope.")
# x = re.findall("The.*2", txt) #search for a sequence(zero or more occurrences)
# print(x)

# x = re.findall("The.+2", txt) #(one or more occurrences)

# x = re.findall("T.?e", txt) #zero or one occurrences
# x = re.findall("r.{2}n",txt) # exactly specified number of occurrences
# x = re.findall("the|The", txt) #parameters
# print(x)


#special sequences
txt = "The rain in spain"
# x = re.findall("\AThe", txt)
# x = re.findall(r"\bain", txt) #\b can be used for beginning&end.
# x = re.findall(r"ain\b", txt)
# x = re.findall(r"\Bain", txt) #\B nor beginning & end.
# x = re.findall(r"ain\B", txt) #\B nor beginning & end.
# print(x)
# if x:
#     print("Yes")
# else:
#     print("No")
# x = re.findall("\D", txt) #opposite of \d
# x = re.findall("\s", txt) #returns white spaces
# x = re.findall("\S", txt) #returns string which doesn't whitespaces (it returned string sentance without spaces)
# x = re.findall("\w",txt) #returns words or 0-9
# x = re.findall("\W", txt) # opposite of \w
# x = re.findall("spain\Z",txt)
# print(x)







#findall()
# text = "The rain in spain"
# x = re.findall("ai", text)
# x = re.search("\s", text) #None will be returned , in case no match
# print(x.start())
# x = re.split("\s", txt, 1)
# print(x)

#sub() - replace the match character 
# x = re.sub("\s", "9", text)
# x = re.sub("\s", "9", text, 2) # we explicitly mention at the end to specify count parameter
# print(x)

#Match object , None will be returned, in-case no match
# x = re.search("ai", text)
# print(x)

text = "The rain in Spain"
#method properties of search
# x = re.search(r"\bS\w+", text)
# print(x.span()) # (start- and end-position) of the first match occurrence (12, 17)

# x = re.search(r"\bS\w+", text)
# print(x.string) #returns(string) - The rain in Spain

# x = re.search(r"\bS\w+", text)
# print(x.group()) #returns word.


