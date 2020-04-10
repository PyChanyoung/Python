matrix = []
col, row = map(int, input().split())
for i in range(row):
    matrix.append(list(input()))
    
from pprint import pprint
pprint(matrix, width=30)