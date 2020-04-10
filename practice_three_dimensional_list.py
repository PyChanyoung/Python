# a = [[[0]*3 for i in range(4)] for i in range(2)]
a = [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
# list = [depth_index][row_index][col_index] = [[[col_index]row_index]depth_index]
print(a)