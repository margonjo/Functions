#Marc Gonzalez
#2/12/14
#1.2

def enter_number():
    num = int(input("please enter an oddnumber: "))
    return num

def Validation(num):
    if num%2 == 0:
        print("this number is even")
    else:
        calculate(num)

def calculate(num):
    space = num
    num = num
    while num >0:
        
        answer = num * "*"
        print("{0:^{1}}".format(answer,space))
        
        num= num -2


def Pyramid():
    num = enter_number()
    Validation(num)

Pyramid()
