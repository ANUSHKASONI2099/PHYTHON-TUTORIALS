# for loop 
# for i in range(5):
#     print()

# else:
#     print("sory no i")

# for i in range(5):
#     print(i)
#     if i ==4:
#         break


# else:
#     print("sory no i")



# # while loop me else 

# i = 0
# while i < 7:
#     print(i)
#     i = i+ 1


# else:
#     print("sory no i")   


# Exception handling 

a = input("Enter the number:")
print(f"muliplication table of {a} is : ")

try:
  for i in range(1, 11):
    print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e: 
    print("Sorry some error occured")


try:
   num = int(input("enter an integer: "))
   a = [6,7]
   print(a[num])
except ValueError:
   print("number entered is not an integer.")

except IndexError:
   print("index error")



