#Marc Gonzalez
#18/11/14
#functions starter

def calculate_basic_pay(hours,pay):
    total = hours * pay
    return total

def calculate_over_time(hours,pay):
    overtime = (hours - 40) * (1.5 * pay)
    basicpay = 40 * pay
    total = basicpay + overtime
    return total

def calculate_total_pay(hours,pay):
    if hours <= 40:
        total = calculate_basic_pay(hours,pay)
    else:
        total = calculate_over_time(hours,pay)
    return total


def get_work_details():
    hours = float(input("please enter the amount of hours you have worked: "))
    pay = float(input("please enter your pay rate: "))
    return hours,pay

def output_pay(total):
    print(total)


def calculate_pay():
    hours,pay = get_work_details()
    total = calculate_total_pay(hours,pay)
    output_pay(total)
calculate_pay()
