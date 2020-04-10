# If create 2d list, assign it to another variable, and change the elements, it will be reflected in both lists
a = [[10, 20], [30, 40]]
b = a
b[0][0] = 500
print(a)
print(b)

# However, if copy the list a to b with the copy method and change the elements of b, both the list a and b are reflected.
a = [[10, 20], [30, 40]]
b = a.copy()
b[0][0] = 500
print(a)
print(b)

# if want to completely copy, have to use deepcopy function in copy module instead of copy method
a = [[10, 20], [30, 40]]
import copy         # get copy module
b = copy.deepcopy(a)    # deepcopy with copy.deepcopy function
b[0][0] = 500
print(a)
print(b)