# list comprehension
# [expression for variable in list]
# list(expression for variable in list)
a = [i for i in range(10)]
print(a)
b = list(i for i in range(10))
print(b)
c = [i + 5 for i in range(10)]
print(c)
d = [i * 2 for i in range(10)]
print(d)

# use if conditional on list comprehension
# [expression for variable in list if condition]
# list(expression for variable in list if condition)
a = [i for i in range(10) if i % 2 == 0]
print(a)
b = [i + 5 for i  in range(10) if i % 2 == 1]
print(b)

# Using for loops and if conditionals multiple times
# [expression for variable1 in list1 condition1   for variable1 in list1 condition1   ...
# for variable(n) in list(n) condition(n)]
# list(expression for variable1 in list1 if condition1  for variable2 in list2 if condition2  ...
# for variable(n) in list(n) condition(n))
a = [i * j for j in range(2, 10) 
           for i in range(1, 10)]
print(a)

# use map on list
# list(map(function,list))
# tuple(map(function, tuple))
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = list(map(int, a))
print(a)

a = list(map(str,range(10)))
print(a)

# input().split() and map
a = input().split()
print(a)

a = map(int, input().split())
print(list(a))