name=input("PLease enter your name: ")
age=int(input("How old are you, {0}? ".format(name)))


if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
    print("*"*50)
else:
    print("Please come back in {0} years".format(18-age))
if age <18:
    print("Please come back in {0} years".format(18-age))
elif age == 900:
    print("Sorry Yoda, you die in Return of the Jedi")
else:
    print("You're old enough to vote")