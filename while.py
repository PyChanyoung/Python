# while basic format
# i = 0                   # initialize
# while i < 100:          # condition
#     print('Hello, world!')  # loop code
#     i += 1              # change

# increment
count = int(input())
i = 0
while i < count:        # loop while i is smaller than count
    print("Hello, world!", i)
    i += 1

# decrement
count = int(input())
while count > 0:            # loop while count is bigger than 0
    print('Hello, world!', count)
    count -= 1              # decrement count by 1

import random       # import random module

i = 0               # initialize index
while i != 3:       # loop while i is not 3
    i = random.randint(1,6)     # create random number between 1 and 6 with randit function
    print(i)

# while loop is useful When the number of repetitions is not fixed

# infinite while loop
while True:
    print('Hello, world!')

while 1:    # not 0 is True
    print('Hello, world!')

while 'Hello':      # Strings with content is True
    print('Hello, world!')

