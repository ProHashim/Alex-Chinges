class Hello:
    # constructor method
    # a method (function that auto executes upon creating an object)
    def __init__(self, color):
        self.color =color
        print(self.color)
    # method
    def say_hello(self):
        self.color = "Green"
        print(self.color)


obj = Hello("White")
obj.say_hello()
