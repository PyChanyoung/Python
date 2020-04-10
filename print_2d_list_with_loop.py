# # with for loop once
# a = [[10, 20], [30, 40], [50, 60]]
# for x, y in a:      # get two elements from one horizontal line in the list (inner list)
#     print(x, y)

# # with for loop 2 times
# a = [[10, 20], [30, 40], [50, 60]]
# for i in a:         # get inner list from a
#     for j in i:     # get elements one by one from the inner list
#         print(j, end = ' ')
#     print()

# # with for and range
# a = [[10, 20], [30, 40], [50, 60]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end = ' ')
#     print()

# # with while loop once
# a = [[10, 20], [30, 40], [50, 60]]
# i = 0
# while i < len(a):       # use size of the list while loop
#     x, y = a[i]         # get two elements in once
#     print(x, y)
#     i += 1              # increment index by 1

# with while loop 2 times
a = [[10, 20], [30, 40], [50, 60]]
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end = ' ')
        j += 1
    print()
    i += 1