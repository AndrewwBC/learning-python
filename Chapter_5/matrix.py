
matrix = [
    [7, 1, 1, 3],
    [7, 1, 9, 2],
    [7, 1, 9, 3],
    [4, 1, 2, 4]
]

dimension = len(matrix)

## range do not reach the value set on the stop parameter
## will always run like, start - stop - 1

for i in range(0, dimension, 1):
    for j in range(0, dimension, 1):
        print(matrix[i][j])