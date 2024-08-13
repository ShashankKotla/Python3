#unordered, unchangable & unindexed , no-duplicate
#Note:Set items are unchangeable, but you can remove items and add new items.

# s = {'one', 5, 5.5, 5}


s = {'one', 5, 5.5, 5, True, 1, False, 0}
# note: True & 1, False & 0 are considered to be same.
# print(s)
# print(len(s))
# print(type(s))

# s2 = set(('two', 2, 3.2))
# print(s2)
# print(type(s2))

#Note : we can't access value through indexing in set.
# we can access through loop or by 'in' keyword

# s = {'one', 'two', 'three'}
# for x in s:
#     print(x)

# print('two' in s)

#methods
s = {'one', 'two', 'three'}
# s.add('four')
# print(s)

# s2 = {"four", "five", "six"}
# s.update(s2) #add one set to another current set.
# print(s)

#Note: update() is for any iterable object.

# s.remove('two')
# s.discard('four')
#note: the only difference of remove & discard, remove gives error if an item don't present. while discard doesn't.
# print(s)

# print(s.pop()) #o/p will be remove item.(with new variable)

# s.clear()
# del s
# print(s)

# for x in s:
#     print(x)


# Join two sets
set1 = {1, 2, 3}
set2 = {3, 4,5}
# set3 = set1.union(set2)
# print(set3)

# set1.update(set2)
# print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# x.intersection_update(y)  #apple
# x2 = x.intersection(y) #apple
#Returns similar items present in both sets
# print(x2)
# print(x)

# x.symmetric_difference_update(y)
# x2 = x.symmetric_difference(y)
#Returns items which are not similar.
# print(x2)

x = {"apple", "banana", "cherry", True}
y = {"google", "microsoft", "apple", 1}

# x.symmetric_difference_update(y) #Note: True & 1 are same
# print(x)


# x.difference_update(y)
# x2 = x.difference(y)
# Returns items(only from first set) which are not similar in both sets.
# print(x2)

# x2 = x.isdisjoint(y)
# Returns True if none of the items are present in both sets, else False.
# print(x2)

# x2 = x.issubset(y)
#returns True if all items are present in both sets
# print(x2)

# x2 = x.issuperset(y)
#Returns True if all items of specified set values in original set.
# print(x2)

# x2 = y.copy()
# print(x2)
# y.clear()
# print(y)
