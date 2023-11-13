# Inheritance: The process of allowing a child class to inheri properties from a parent class.

# global variable
# One of the type of scope -> Global scope
#  This variable is defined outside of any block / function that is why we call it globally defined variable.
math = "Fav subject"

class Person:
    # content of the class
    def __init__(self, person_name):
        # a property has been initialized
        # Local scope
        # Because this is defined inside of a block / function.
        self.person_name = person_name
        # this print will work
        # print(person_name)
    
    # not defined error
    # print(person_name)
    # print(self.person_name)



# Define an object (instance)
alex = Person("Alex")
print(alex.person_name, " from line 19")


# the Alex class is inheriting Person class.
class Alex(Person):
    pass