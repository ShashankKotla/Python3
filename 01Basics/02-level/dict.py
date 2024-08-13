#ordered, changeable, no-duplicates

# d = {
#     'brand': "Tesla",
#     'model' : "model7",
#     'year' : 2024,
#     'brand' : "Tesla"
# }
# print(d)
# print(len(d))
# print(type(d))
# print(d['brand'])




#values in dictionary items can be of any DT
# d = {
#     'brand': "Tesla",
#     'model' : "model7",
#     'year' : 2024,
#     'colors' : ['red', 'white', 'blue']
# }
# # print(d)

# d2 = dict(name = 'john', age = 22) #type conversion
# print(d2)


#Accessing items

# x = d.get('brand')
# x = d.keys()
# x = d.values()
# print(x)
# print(d.items()) #dict_items([('brand', 'Tesla'), ('model', 'model7'), ('year', 2024), ('colors', ['red', 'white', 'blue'])])


# d['brand'] = "Benz"
# print(d)


# d['month'] = "march"
# print(d)

# d['animal'] = 'Elephant' #addon new item to original dict
# print(d)

# if 'brand' in d:
#     print("Yes It is present")
# else:
#     print("No it is not present")


#Methods

#update the values (2ways)
# d['brand'] = 'Benz'
# print(d)

# d.update({'brand' : "BMW"})
# print(d)


#Removing Items
# d = {
#     'brand': "Tesla",
#     'model' : "model7",
#     'year' : 2024,
#     'colors' : ['red', 'white', 'blue']
# }

# d.pop('year') #removes specified item
# d.popitem() #removes last item
# print(d)

# del d['brand'] #deletes specified item
# print(d)

# d.clear()
# print(d)


#Looping 
# d = {
#     'brand': "Tesla",
#     'model' : "model7",
#     'year' : 2024,
#     'colors' : ['red', 'white', 'blue']
# }

# for x in d:
#     print(x) #returns keys.

# for x in d:
#     print(d[x]) #Returns values

# for x in d.keys():
#     print('keys:',x)

# for y in d.values():
#     print('values: ' ,y)

#To return full items()
# for x, y in d.items():
#     print(x,':', y)

#copy method
# d = {
#     'brand': "Tesla",
#     'model' : "model7",
#     'year' : 2024,
#     'colors' : ['red', 'white', 'blue']
# }

# myd = d.copy()
# print(myd)

# myd = dict(d)
# print(myd)

#Nested Dictonary - We can provide more then one dictionary object-scopes

myfamily = {
    'child1' : {
        'name' : 'email',
        'year' : 2004
    },
    'child2' : {
        'name' : 'gmail',
        'year' : 2005
    },
    'child3' : {
        'name' : 'call',
        'year' : 2007
    }
}

# print(myfamily)

#Adding 3dictionaries to another new dict

child1 =  {
        'name' : 'email',
        'year' : 2004
    }
child2 = {
    'name' : 'gmail',
    'year' : 2005
    },
child3 = {
    'name' : 'call',
    'year' : 2007
    }

myfamily2 = {
    'child1' : child1,
    'child2': child2,
    'child3' : child3
}
# print(myfamily2)

#Accessing items from Nested Dict
# print(myfamily2['child1']['year'])

#fromkeys - returns a dictionary with the specified keys and the specified value.
x = {'one', 'two', 'three'}
y = 0
# dd = dict.fromkeys(x, y)
# print(dd)
# x2 = {'two':2}
# x2.update({'three': 3})
# print(x2)


#Methods of dict
# clear, copy(), fromkeys(), get(), keys(), values(), pop(), popitem(), update(), setdefault()