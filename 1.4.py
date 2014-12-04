#Marc Gonzalez
#4/12/14
#1.4

def fahrenheit():
    temp = int(input("please enter the tempreture in fahrenheit: "))
    return temp

def celsius():
    temp = fahrenheit()
    temp2 = temp - 32
    celsius = temp2 * (5/9)
    print(celsius)

celsius()
