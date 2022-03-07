low=1
high=1000

print('Please think of a number between {} and {}'.format(low, high))
input('Press ENTER to start')

guesses=1
while True:
    guess= low+ (high-low)//2
    high_low= input("My guess is {}. Should I guess higher  or lower? "
    "Enter h or l or c if my guess was correct "
    .format(guess)).casefold()

    if high_low=='h':
        #Guess higher. the low end of the range becomes 1 greater than the guess
        low= guess+1
    elif high_low=='l':
        high= guess-1
        #guess lower. the  high end of the range becomes one less than the guess
    elif high_low=='c':
        print(' I got it in {} guesses!'.format(guesses))
        break
    else:
        print('Please enter h, l or c')
    guesses= guesses+1

