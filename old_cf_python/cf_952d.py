def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))


def solve():
    n, m = invr()
    matrix = []
    for _ in range(n):
        row = insr()
        matrix.append(row)
    maxRowLength = 0
    maxRow = 0
    for i in range(n):
        rowLength = 0
        for j in range(m):
            if matrix[i][j] == "#":
                rowLength += 1
        if rowLength > maxRowLength:
            maxRowLength = rowLength
            maxRow = i
    count = 0
    for i in range(m):
        if matrix[maxRow][i] == "#":
            count += 1
        if count == maxRowLength // 2 + 1:
            print(str(maxRow + 1) + " " + str(i + 1))
            break

            

for _ in range(inp()):
    solve()