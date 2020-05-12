# [
#     123
#     456
#     789
# ]

''' this is a 3x3 matrix in math. 2D (arrays) lists are lists 
that has a list within a list'''

matrix = [
    [1,2,3],
    [4,6,7],
    [5,6,7]
]
# matrix [0][1] = 20
''' this is to modify '''

# print(matrix [0][1]) 
'''this will print out the one number in the 1st list [0] and the [1] will print out the 2 in the (array) list'''

for row in matrix:
    for item in row:
        print(item) 
''' we can also use nested loops to itorate all the items in a 2D (array) list '''



