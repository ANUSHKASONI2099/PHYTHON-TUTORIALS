# function 
# def calculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     print (mean)

# def isGreater(a,b):
#   if(a>b):
#         print("First number is greater")
#   else:
#         print("Second number is greater or equal")
# a = 8
# b= 13
# isGreater(a,b)
# calculateGmean(a,b)

# def islesser(a,b):
    #  pass
# gmean1 = (a*b)/(a+b)
# print(gmean1)
# c = 14
# d = 18
# isGreater(c,d)
# calculateGmean(c,d)



# def average(a=8,b=9):
    # print("The average is ", (a+b)/2)
# average()

# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#         # print("Average is :", sum/len(numbers))
#         return sum / len(numbers)




# c = average(5,5,6,7)
# print(c)


# Lists.....


l =[3,55,6,9,78]
# print(l)
# print(type(l))
# print(l[1])

# negative index 
# print(l[-3])
# print(l[len(l)-3])

# if 55 in l:
#     print("yes")
# else:
#     print("no")

# if 5 in 55:
#         print("yes")

# jump index 
# print(l)
# print(l[1:4])
# print(l[1:4:3])

# lst = [i*i for i in range(10)]
# print(lst)
# lst = [i*i for i in range(10) if
#        i%2==0]
# print(lst)


# l = [1,2,4,7,8,4,6,7]
# print(l)
# # l.append(8)
# l.sort()
# l.reverse()
# print(l.index[3])
# print(l.count(1))

# m = l.copy()
# m[0] = 0

# l.insert(1,66)

# l.pop(3)

# m = [9,70,89]
# k = l+m
# print(k)
# l.extend(m)



# print(l)


# tuples- that cannot be change

tup = (1,8,9)
print(type(tup), tup)

print(tup[1])
# print(tup[3])

if 8 in tup:
    print("yes")
tup2 = tup[1:3]
print(tup2)