#Marc Gonzalez
#2/12/14
#1.2
import pdb
def enter_number():
    num = int(input("please enter an oddnumber: "))
    return num
def Validation(num):
    if num%2 == 0:
        print("this number is even")
    else:
        actual_p(num)
def Pyramid():
    num = enter_number()
    Validation(num)
def actual_p(num):
    diamond = "*"
    num1 = num * "*"
    while num1 != diamond:
        print("{0:^{1}}".format(diamond, num))
        diamond = diamond +"**"
    space = num
    num = num
    while num >0:
        answer = num * "*"
        print("{0:^{1}}".format(answer,space)) 
        num= num -2        
    num6 = num*10
    tree = "*" 
    
    while num6 != tree:
        print("{0:^{1}}".format(tree, num))
        tree = tree +"**"
pdb.set_trace()
Pyramid()
