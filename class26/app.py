# this is a class where we are creating a blueprint for taking the user's name and their message.
class Message:
    names = input("What is your name? ")
    user_message = input("Your message: ")


# user is an object
user = Message()
print("Your name is: ", user.names)
print("Your message is:",  user.user_message)