# Operation on tuple 

# if you want to change tuple so convert it into list and then change after that list convert into tuple 
# tuple = (0,1,3,5,6,3,8,3,3,6)
# res = tuple.count(3)
# res = tuple.index(3,4,6)
# # res = tuple.index(3)
# res = len(tuple)
# print('count of 3 in tuple is: ',res)

# f-string method-use in string formating 

# letter = "hey my name is {} and i am from {}" 
# country = "india "
# name = "anushka"
# print(letter.format(name,country))
# print(f"hey my name is {name} and i am  from {country}")

# print(f"hey my name is {{name}} and i am  from {{country}}")
# price = 49.003000
# txt = (f"for only {price:.2f} 
# dollars!")
# print(txt)

# print(f"{2 * 67}")


# Doc strings and P

def square(n):
    '''Takes in a number n , returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

