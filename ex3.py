from ex3 import question

# Create a progarm capable of displaying question to the user like KBC 
# use list data type to store questions and correct answer 
# display the final amount the pertson is taking home after playing the game ........


questions = [
["which language was used to create fb?", "python", "french" , "javascript" , "php" , "none ", 4]



["which language was used to create fb?", "python", "french" , "javascript" , "php" , "none ", 4]


["which language was used to create fb?", "python", "french" , "javascript" , "php" , "none ", 4]

]

levels = [ 1000 , 2000, 3000, 5000, 10000, 20000 , 40000 , 8000, 160000, 320000]


for i in range(0 , len(questions)):
    question = questions[i]
    print(f"question for Rs. {levels[i]}")
    print(f"a. {question[i][1]}                     b. {question[i][2]}")
    print(f"c. {question[i][3]}                      d. {question[i][4]}")
reply = int(input("Enter your answer (1-4) "))

if(reply == question[-1]):
   print(f"Correct answer, you have won Rs. {levels[i]}")
   if(i == 4):
     money = 10000
   elif (i == 9):
     money = 320000
else:
  print("Wrong answer") 
break
 

print(f"your take home money is {money}")