from collections import defaultdict
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

matrix = []
n = inp()
for _ in range(n):
    row = insr()
    matrix.append(row)

rows = len(matrix)
cols = len(matrix[0])

def path(r, c, dir):
    if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] == "X" or matrix[r][c].isdigit():
        return True
    if matrix[r][c] == "?":
        return False
    x, y = dir
    vis.add((r,c))
    ans = path(r + x, c + y, dir)

    return ans
    


vis = set()
good = True
directions = [[1,0],[0,1],[0,-1],[-1,0]]
#no two lightbulbs can shine on each other (recursion)
for r in range(rows):
    for c in range(cols):
        if matrix[r][c].isdigit():
            bulbs = 0
            for x,y in directions:
                if 0 <= (r + x) < rows and 0 <= (c+y) < cols and matrix[r+x][c+y] == "?":
                    bulbs += 1
            if bulbs != int(matrix[r][c]):
                good = False
        if matrix[r][c] == "?":
            for d in directions:
                if not path(r + d[0], c + d[1], d):
                    good = False


for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "." and (r,c) not in vis:
            good = False

if not good:
    print("0")
else:
    print("1")

    


    
#every blocked cell with a number must have that number of lightbulbs adjacent
    
#every open cell is lit (visited set)
        
        
