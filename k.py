# Dictionary -is collection key value pairs 
dic = {
    # "anushka":"Human being",
    # "spoon":"object"
    321: "annu"
    # there 321 is key and annu is value 
}
print(dic[321])

info = {'name':'anushka','age' :'18', 'elligible':'true'}
# print(info)
# # error thruogh krega 
# print(info['name'])
# # error through nhi krega 
# print(info.get('name'))

# print(info.keys())
 
# for key in info.keys():
#     print(info[key])

#     print(info.values())

# for key in info.keys():
#     print(f"the value corresponding to the key {key} is {info[key]}")

# print(info.items())
# for key , value in info.items():
#     print(f"the value corresponding to the key {key} is {value}")
 

# dictinory methods 
# dictionary ordered hoti and sets unordered hoti 
a = {100: 14, 160: 61, 690: 45, 479: 78}
b = {212: 14, 230: 71}
a.update(b)
print(a)

# if you want to clear dictionar use "clear "
a = {100: 14, 160: 61, 690: 45, 479: 78}
b = {212: 14, 230: 71}
a.clear()
print(a)


# if you want remove one key value pair use "pop"
a = {100: 14, 160: 61, 690: 45, 479: 78}
b = {212: 14, 230: 71}
a.pop(100)
print(a)


# if you want delete last key value pairs use "pop-item" 

a = {100: 14, 160: 61, 690: 45, 479: 78}
b = {212: 14, 230: 71}
a.popitem()
print(a)

# del use for delete dictionary 

a = {100: 14, 160: 61, 690: 45, 479: 78}
b = {212: 14, 230: 71}
del a()
print(a)















