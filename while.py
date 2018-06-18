# for  i in range(10):
#     print("i is now {}".format(i))
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i +=1
# available_exits = ["east", "north east", "south"]
#
# choosen_exit = ""
# while choosen_exit not in available_exits:
#     choosen_exit = input("please choose a direction")
#     if choosen_exit == "quit":
#         print("Game over")
#         break
# else:
#     print("aren't you glad you got out of there!")
import random
highest = 10
answer = random.randint(1,highest)

print("please guss a number between 1 and {}:".format(highest))
guess = 0
while guess != answer:
    guess = int(input())
    if guess <answer:
        print("please guess higher")
    elif guess> answer:
        print("please guess lower")
    else
        print("well done , you guess it")
