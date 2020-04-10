# get specific index on tuple
a = (38, 21, 53, 62, 19, 53)
print(a.index(53))

# counting specific value
a = (10, 20, 30, 15, 20, 40)
print(a.count(20))

# print out with for loop
a = (38, 21, 53, 62, 19)
for i in a:
    print(i, end = '    ')

# use tuple comprehension
# tuple(expression for variable in list if condition)
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

# use map on tuple
a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int,a))
print(a)

# get munimum, maximum and sum
a = (38, 21, 53, 62, 19)
print(min(a))
print(max(a))
print(sum(a))