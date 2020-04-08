# break : finish the loop

# How to use break in while loop
i = 0
while True:         # infinite loop
    print(i)
    i += 1          # increment i by 1
    if i == 100:    # if i is 100,
        break       # finish the loop. 

# How to use break in for loop
for i in range(10000):  # loop from 0 to 9999
    print(i)
    if i == 100:        # if i is 100,
        break           # finish the loop

# continue in for loop
for i in range (100):   # loop 100 times increment from 0 to 99
    if i % 2 == 0:      # it is even, if divided by 2 and remainder is 0
        continue        # skip without executing below code
    print(i)

# continue in while loop
i = 0
while i < 100:          # loop while i is smaller than 100. loop 100 times increment from 0 to 99
    i += 1              # i increment by 1
    if i % 2 == 0:      # it is even, if divided by 2 and remainder is 0
        continue        # skip without executing below code
    print(i)

# pass
for i in range(10):     # loop 10 times
    pass                # do nothing

while True:             # infinite loop
    pass                # do nothing

# loop as many times as input
count = int(input())
i = 0
while True:         # infinite loop
    print(i)
    i += 1
    if i == count:  # if i is same with input,
        break       # finish the loop

# Output odd numbers up to input numbers
count = int(input())

for i in range(count + 1):      # loop from 0 to count(count + 1), increasing from 0
    if i % 2 == 0:              # it is even, if divided by 2 and remainder is 0
        continue                # skip without executing below code
    print(i)