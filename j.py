# sets ....it is collection of well defined objects and repeated value does not print
#  and doest not gurrenti for order of values and they arec unchangble 

# s = {3,6,7,2,2}
# print(s)
 


# a = {"annu", 2, 67,5,7 ,5}
# print(a)
# print(type(a))

# annu = set()
# print(type(annu))










# for value in a:
#     print(value)

# Sets method 
# s = {3,4,5,7}
# s2 = {2,4,6}
# print(s.union(s2))
# print(s.difference(s2))

# disjoint sets - sets are the set which do not have any bussiness or intersection with each other

a = {"tokoyo" ,"mumbai","delhi","agra"}
b = {"allahabad","lucknow","delhi","tokoyo"}
print(a.isdisjoint(b))


# superset 

a = {"tokoyo" ,"mumbai","delhi","agra"}
b = {"allahabad","lucknow","delhi","tokoyo"}
c = {"delhi","allahabad","lucknow"}
print(a.issuperset(b))
print(b.issuperset(b))

# if you want to add single items in set use "add"\

a = {"annu","aashi"}
a.add("aadi")
print(a)

# if you want to add more than one item use "update" 
# a = {"annu","aashi"}
# a.update("aadi","aaradhya")
# print(a)

# if you want to remove something on your items use "remove" 

a = {"mango","apple","pineapple"}
a.remove("apple")
print(a)

# 'the main deference between remove and discard is that ,if we try to delete an item which is not present in set' remove raise an error,whereas discard does not raise any error

# pop method - this method removes the last item of the set but the catch is that we don't know which item gets popped
a = {"arti","kanish","radha","annu"}
b = a.pop()
print(a)
print(b)

# if you want to delete something in your item use "del" keyword
a = {"arti","kanish","radha","annu"}
del a
print(a)

# if we want to does'nt delete entire set if we want to delete items present in set use "clear"
a = {"arti","kanish","radha","annu"}
a.clear()
print(a)

