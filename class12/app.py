# List

my_list = []


# tuple
my_tuple = (56, 78, "hello", True)


# Set
# unordered, unchangeable, NO duplicates
my_set = {
    "Item 1", 23, "sdfsg", False, 23
}

# print(my_set)

# print(len(my_set))

# print(type(my_set))

cars = set(
    (
        "Toyota", "Honda", "MB"
    )
)
# print(type(cars))

# wether an Item exist or not
# print("Honda" in cars)

# cars.add("Chevy")

cars2 = set(
    (
        "Brabus", "Jeep", "Jaguar"

    )
)

cars.remove("Honda")

cars.update(cars2)
print(cars)

drinks = set(
    ("Coca Cola", "Fanta", "sprite")  
)
