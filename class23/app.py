# expression
a = 5

# statement
if 1 > 5:
    print()


def fun(a):
    return a


print(fun(5))

# numeric values
print(5 + 6)

# we have assigned 5 to the variable a where a is returning 5 as its value so the following addition of a and 6 would work as a = 5, so this mean 5 + 6.
print(a + 6)


def even_nums():
    for number in range(50):
        # modulo operator (%)
        if number % 2 == 0:
            print(number)


even_nums()
