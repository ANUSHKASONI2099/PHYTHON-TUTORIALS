# Seek()functions 

with open('file.txt','r') as f :
    print(type(f))
    # move to the 10th byte in the file

    f.seek(10)

    # Read the next 5 bytes 

    # tell() function -konsi postion se seek kiya like here after 10 elements
    print(f.tell())
    data = f.read(5)
    print(data)



# truncate use for - kitne characters rakhna chahte hai hm apne sentence me 

with open('a.txt','w') as f :
    f.write('Hello everyone')
    f.truncate(4)

with open('a.txt','r') as f :
    print(f.read())


