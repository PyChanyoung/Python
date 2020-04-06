# animal package
# dog, cat modules
# doc, cat modules can say "Hi"

# from animal import dog      # get the dog module from animal pacakge
# from animal import cat      # get the cat module from animal pacakge

from animal import *        # get every modules from animal package

d = Dog()
c = Cat()
d.hi()
c.hi()
# d = dog.Dog()
# d.hi()

# c = cat.Cat()
# c.hi()