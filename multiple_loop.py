# for i in range(5):      # loop 5 times. Outer loop is height
#     for j in range(5):  # loop 5 times. Inner loop is width
#         print('j:', j, sep = '', end = '    ')     # output j.
#     print('i:', i, '\\n', sep = '')     # output i.

# # star_square.py
# for i in range(5):
#     for j in range(5):
#         print('*', end = '  ')
#     print()

# star_triangle.py
for i in range(5):
    for j in range(5):
        if j <= i:
            print("*", end = '  ')
    print()

for i in range(5):
    for j in range(5):
        if j >= i:
            print("*", end = '  ')
    print()

for i in range(5):
    for j in range(5):
        if j < i:
            print(" ", end = '  ')
        else:
            print("*", end = '  ')
    print()

# star_diagonal.py
for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end = '  ')
        else:
            print(' ', end ='   ')
    print()