#Marc Gonzalez
#4/12/14
#1.3

def numbers():
    num1 = int(input("please enter a number: "))
    num2 = int(input("please enter another number: "))

    return num1, num2


def calculate(num1, num2):
    if num1> num2 :
        print(num2, num1)
    else:
        print(num1, num2)
def sort():
    num1, num2 = numbers()
    calculate(num1, num2)



sort()
