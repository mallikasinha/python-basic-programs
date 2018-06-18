# name = input("please enter your name:")
# age = int(input("how old are you, {0}?".format(name)))
# print ("oh!! so you are {0}".format(age))
#
# if age >=18:
#     print("you are old enough to vote")
#     print("please put an X in the box")
# else:
#     print("you cant vote.please  come in {0} years".format(18-age))
print("please guss a number between 1 and 10:")
guess = int(input())
n
if guess != 5:
    if guess <5:
        print("please guess higher")
    else:
        print("please guess lower")

        guess = int(input())
        if guess ==5:
            print("well done , you guess it")
        else:
            print("Sorry you have not guesses correcly")

    else:
        print("you got it frst time")
