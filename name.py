def get_matrix(n,m,value):
    matrix= []
    for i in range(n):
        row=[]
        for i in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
n=3
m=3
value=4
matrix = get_matrix(n, m, value)
print(matrix)
