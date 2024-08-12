from k import info

# Write a python progrogramm to translate a message into secert code language .use that rules below to translate normal english into secret code language 

# coding:
# if the word contains atleast 3 characters ,remove the first letter and append it at the end now append three random characters at th starting and the End 
# else:
#     simply reverse the string 


#     decoding:
#     if the word contains less than 3 characters ,reverse it 
# else:
# remove 3 random character from start and end .now remove the last letter

st = "anushka is a good girl"
coding = True
if(coding):
    if(len(st)>=3):
        r1 = "ans"
        r2 ="dsj"
        st = st[1:] +st[0] +r2
        print(st)
else:


pass