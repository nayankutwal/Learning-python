answer=5

print("Please guess a number between 1 and 10: ")
guess=int(input())

if guess == answer:
    print("Great! You got it in the first try!")
else:
    if guess<answer:
        print("Please guess higher")
    else:  # guess must be greater than answer
        print("Please guess lower")
    guess= int(input())
    if guess==answer:
        print("Well done! you guessed it")
    else:
        print("Game over")

# if guess < answer:
#      print("Please guess higher")
#      guess=int(input())
#      if guess ==answer:
#          print("Well done, you guessed it")
#      else:
#          print("Sorry, you've not guessed correctly. ")
# elif guess > answer:
#      print("Please guess lower")
#      if guess ==answer:
#          print("Well done, you guessed it")
#      else:
#          print("Sorry, you've not guessed correctly. ")
# else:
#      print("You got it first time!")
