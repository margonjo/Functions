#Marc Gonzalez
#4/12/14
#2.3

def get_currency():
    currency = input("please enter the symbol for the currency you wish to convert: ")
    convert_to = input("please enter the symbol for the currency you wish to convert too: ")
    return currency, convert_to

def calculate(currency, convert_to):
    if currency == "£" :
        if convert_to == "€":
            amount = float(input("please enter the amount of pounds you want to convert: "))
            final_amount = amount * 1.229
            print("you have € {0}".format(final_amount))
        elif convert_to == "$":
            amount = float(input("please enter the amount of pounds you want to convert: "))
            final_amount = amount * 1.601
            print("you have $ {0}".format(final_amount))

        else:
            print("please selsct an appropriate symbol")
            
