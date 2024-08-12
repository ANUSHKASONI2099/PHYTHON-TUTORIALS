# file I/o 


# Reading file 

# f = open('myfile.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.closed()


# Writing file 


# f = open('myfile.txt', 'w')
# f.write('Helloo , world!')
# f.close()


# other method 

# with open('myfile.txt','a') as f:
#     f.write("Hey I am inside with")


# # Read line 
# f = open('myfile.txt', 'r')
# i = 0
# while True:

#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     line = f.readlines()
#     m1 =line.split(",")[0]
#     m2 =line.split(",")[1]
#     m3 =line.split(",")[2]
#     print("Marks of student {i} in maths is : {m1}")
#     print("Marks of student {i} in English is : {m2}")
#     print("Marks of student {i} in S.S.T is : {m3}")

#     print(line)

f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close


