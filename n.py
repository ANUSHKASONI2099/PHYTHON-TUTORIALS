# shorthand if else in one line
# a = 340000
# b = 423
# print("A") if  a>b else print("=") if a == b else print("B")


# c = 9 if a>b else 0
# print(c)

# enumerate function
# marks = [12, 23,5,78,94,51]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("anushka, awesome!")
#         index +=1




marks = [12, 23,5,78,94,51]

# index = 0
# for index, mark in enumerate(marks):  
for index, mark in enumerate(marks , start = 1):
    print(mark)
    if(index == 3):
        print("anushka, awesome!")
        index +=1
























