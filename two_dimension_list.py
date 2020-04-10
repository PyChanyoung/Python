# # create 2 dimensional list and access elements
# # list = [[value, value], [value, value], [value, value]]
# a = [[10, 20], 
#      [30, 40], 
#      [50, 60]]
# print(a)

# # accessing elements of 2 dimensional list
# # list[row_index][col_index]
# # list[row_index][col_index] = value
# a = [[10, 20], [30, 40], [50, 60]]
# print(a[0][0])
# print(a[1][1])
# print(a[2][1])
# a[0][1] = 1000
# print(a[0][1])
# print(a)

# # jagged list
# a = [[10, 20], [500, 600, 700], [9], [30, 40], [8], [800, 900, 1000]]
# print(a)

# continue from this page tomorrow
# 20200410 10:25
a = [[10, 20], [30, 40], [50, 60]]
from pprint import pprint
pprint(a, width=20)