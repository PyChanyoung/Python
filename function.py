# First, get the name and age
# If age is below 10, say "Hi"
# If age is between 10 and 20, say "Hello"
# else, "Greeting"

def SayHello(name, age):
    if age < 10:
        print("Hi " + name)
    elif age <=20 and age >= 10:
        print("Hello " + name)
    else:
        print("Greeting " + name)

SayHello("Wonnie", 9)