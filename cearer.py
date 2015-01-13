#Marc Gonzalez
#20/12/14
#function2


def get_shift_message():

    what = input("would you like to decypt or encrypt ('d' 'e'): ")

    shift = int(input("what shift would you like to encrypt with: "))
    message = input("what message would you like to encrypt: ")

    return shift, message , what

def encryption( shift , message, what):

    newmessage = ""
    if what == "d":
        shift = -shift
    
        
    for letter in message:
        if letter.isalpha:
            number = ord(letter)
            new = number + shift
            
            if letter.isupper():
                if new > ord("Z"):
                    new -= 26

                elif new < ord("A"):
                    new += 26
            elif letter.islower():
                if new > ord("z"):
                    new -= 26

                elif new < ord("a"):
                    new += 26
            
            newmessage = newmessage + chr(new)
    print (newmessage)
                
                


            
            







shift, message, what = get_shift_message()

encryption( shift , message, what )
