# lcture 52
# Lambda functions

# def double(x):
    # return x*2

# double = lambda x: x*2

# avg = lambda x,y: (x+y)/2
# cube = lambda x: x*x*x

# print(cube(6))
# print(double(5))
# print(avg(5,5))






# lecture 53
# Map ,filter and reduce 
 

# Map - it is a higher oredre function
# def cube(x):
#     return x*x*x


# print(cube(2))

# l = [1,2,3,4,5,6,7]
# # newl = []
# # for item in l :
# #  newl.append(cube(item))
# newl = list(map(cube , l))
# print(newl)



# # Filter  it is higher order function
# def filter_function(a):
#     return a>3

# newnewl = list(filter(filter_function,l))
# print(newnewl)

# Reduce 
# from functools import reduce 

# numbers = [1,3,4,5,7,2,8]

# def mysum(x,y):
#     return x+y

# sum = reduce(mysum,numbers)

# print(sum)
# print the sum


# lecture 54 
# 'is'- it compares exact location of  object in memory and '==' - compare the values

# a = [1,2,34]
# b = [1,2,34]

# a = "anuu"
# b = "anuu"


a = None
b = None

print(a is b)
print(a==b)


