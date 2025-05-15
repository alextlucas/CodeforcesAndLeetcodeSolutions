def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


N = inp()
matrix = []
for _ in range(N):
    row  = inlt()
    matrix.append(row)

res = 0

for i in range(N):
    ones = 0
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            ones += 1
    if ones >= 2:
        res += 1

print(res)




