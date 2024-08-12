# finallly clause - always execute ...doubt see again becoz most imp for interviews
# def func():

#     try:
#         a = [1,2,3,4,5]
#         b = int(input("Enter the index: "))
#         print(a[b])
#         return 1
#     except:
#         print("some error ocured")
#         return 0

#     finally:
#         print("I am always executed")


# x = func()
# print(x)


#  raising Coustom errors 

a = int(input("enter any value between 5 and 9"))

if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")


# coustom Exception
