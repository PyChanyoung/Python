# # list_create.py
# a = []      # create blank list
# for i in range(10):
#     a.append(0)     # add elements with append
# print(a)

# # two_dimensional_list_create.py
# a = []      # create blank list
# for i in range(3):
#     line = []       # create blank list for use inner list
#     for j in range(2):
#         line.append(0)      # add 0 to inner list
#     a.append(line)          # add inner list to overall list
# from pprint import pprint
# pprint(a, width=20)

# # create 2D list with list comprehension
# a = [[0 for j in range(2)] for i in range(3)]
# from pprint import pprint
# pprint(a, width=20)

# a = [[0] * 2 for i in range(3)]
# from pprint import pprint
# pprint(a, width=20)

# jagged_list_create.py
a = [3, 1, 3, 2, 5]
b = []
for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)
print(b)
# jagged_list_create_with_list_comprehension.py
a = [[0] * i for i in [3, 1, 3, 2, 5]]
print(a)

# sort 2D list by sorted()
# sorted(object loopable, key = sort function, reverse=True or False)
students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 17]
]
print(sorted(students, key = lambda student: student[1]))
print(sorted(students, key = lambda student: student[2]))