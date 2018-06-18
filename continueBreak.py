# shopping_list = ['milk','pasta','egs','spam','bread','rice']
# for item in shopping_list:
#     if item == 'spam':
#         print("I am ignoring {}".format(item))
#         continue#bypasses that value
#     print("Buy " +item)


# shopping_list = ['milk','pasta','egs','spam','bread','rice']
# for item in shopping_list:
#     if item == 'spam':
#         break
#     print("Buy "+item)


meal = ["egg","bacon","sausages","tomato","spam"]
nasty-food_item =''
for item in meal:
    if item == "spam":
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then,please")
if nasty_food_item =="spam":
    print("can i have anything without spam in it")
