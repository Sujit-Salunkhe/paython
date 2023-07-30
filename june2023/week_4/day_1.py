matrix = [
    [2, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
]
# print(len(matrix))
x=0
for i in range(len(matrix)):
    x +=(matrix[i][i])

j=0
y=0
for i in range(len(matrix)-1,-1,-1):
    y +=(matrix[j][i])
    j +=1
print(x - y)