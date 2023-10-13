# if elif else

if 1 > 3:
    print()

elif 1 > 5:
    print()

elif 1 > 6:
    print()

else:
    # print("It is not working")
    print()

# if 1<4:
    # print("Yes it is less than 4")

# identifier
car = "Bugatti"

# Functions

# def is a keyword
# Function name is myFun() and we can call this name as an identifier


def myFun():
    # function body
    print("I am in a function")


# function call
myFun()

# parameter
def hello(name, age):
    print("Hello, ", name, "and your age is ", age)


# argument (args)
hello("Eli", 33)



# Arbitrary arguments (*args)
def hi(*info):
    print("Hello, ", info[0], "and your age is ", info[1], "and your height is ", info[2])


# argument (*args)
hi("Ali", 3, 1.3)


def fun():
    q = "l"
    print(q, "1234567890")


fun()
