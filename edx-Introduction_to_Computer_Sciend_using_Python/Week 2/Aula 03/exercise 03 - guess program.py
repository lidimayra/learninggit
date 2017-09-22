print('Please think of a number between 0 and 100')

high   = 100
low    = 0

while True:
    number = (high + low) // 2

    print('Is your secret number %s?' % (number))

    value = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if(value == 'l'):
        low = number
    elif(value == 'h'):
        high = number
    elif(value == 'c'):
        break
    else:
        print('Sorry, I did not understand your input.')
    
    
print('Game over. Your secret number was: ', number)