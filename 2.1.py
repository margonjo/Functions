#Marc Gonzalez
#4/12/14
#2.1

def input_time():
    hours = int(input("please enter the number of hours: "))
    minutes = int(input("please enter the nunber of minutes: "))
    seconds = int(input("please enter the number of seconds: "))
    return hours, minutes, seconds

def seconds_calculate( hours, minutes, seconds):
    seconds_hours = hours * 3600
    seconds_minutes = minutes * 60

    total_seconds = seconds_hours + seconds_minutes + seconds

    print(total_seconds)

def total_seconds():
    hours, minutes, seconds = input_time()
    seconds_calculate( hours, minutes, seconds)

total_seconds()
