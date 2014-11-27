# functions improvement exercise
# times-table tester
import random

### main program
###print("Times-table tester")
###print()
##testTable = input("Which times-table do you want to be tested on? ")
##testTable = int(testTable)
##for questions in range(1,6):
##    Num1 = testTable
##    Num2 = random.randrange(2,13)
##    Ans = Num1 * Num2
##    UserAnswer = input(str(Num1) + ' x ' + str(Num2) + ' = ? ')
##    UserAnswer = int(UserAnswer)
##    if UserAnswer == Ans:
##        print('Well done, you got the correct answer!')
##        print()
##    else:
##        print('Sorry, you got the answer wrong. The correct answer is',Ans)
##        print()
##              
def input_answer(Num1,Num2):
     UserAnswer = int(input(str(Num1) + ' x ' + str(Num2) + ' = ? '))
     return UserAnswer


def Actual_answer(Num1,Num2):
    Ans = Num1 * Num2
    return Ans

def Timestable_display(Num1,Num2):
    if Actual_answer(Num1,Num2) == input_answer(Num1,Num2):
        print('Well done, you got the correct answer!')
    else:
        print('Sorry, you got the answer wrong. The correct answer is {0}'.format(Actual_answer(Num1,Num2)))

def input_timestable():
    Num1 = int(input("Which times-table do you want to be tested on? "))
    return Num1
def Timestable_Tester(testtable):
     Num2 = random.randrange(2,13)
     Num1 = testtable
     Ans = Actual_answer(Num1,Num2)
     Timestable_display(Num1,Num2)
    
def generate_questions():
     testtable = input_timestable()
     for questions in range(1,6):
          Timestable_Tester(testtable)
generate_questions()
