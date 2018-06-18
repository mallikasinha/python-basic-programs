age = 24
print("My age is" + str(age) + "years")#str convert integer to string

print("My age is {0} year".format(age)) #replacement field
print("there are {0} days in {1} ,{2} {3} {4}".format(31, "jan", "feb", "march", "may"))

print("""Jan: {2}
Feb: {0}
March: {2}
April: {1}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}
""".format(28,30,31))
print("My age is %d year" % age)
print("My age is %d %s, %d, %s" %(age, "year" , 6,"month")) #used in python 2

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %d"%(i, i**2, i**3))
print("PI is approximately %12.50f" %(22 / 7))

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:3}".format(i, i**2, i**3))

print("PI is approximately {0:12.50}".format(22 / 7))

for i in range(1, 12):
    print("No. {} squared is {} and cubed is {}".format(i, i**2, i**3))
