mat = [[1,2,3],[4,5,6],[7,8,9]]
n=3
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(n):
    for j in range(n):
        result[j][n-i-1]=mat[i][j]
for row in result:
    print(row)
