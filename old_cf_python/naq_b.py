def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

min_y = [float("inf")]

def solve():
    x1, y1, x2, y2 = invr()
    if x2 - x1 != 0:
        slope = (y2 - y1) / (x2 - x1)
        y_int = (y1 - (slope * x1))
        if y_int > 0 and ((x1 >= 0 and x2 <= 0) or (x1 <= 0 and x2 >= 0)):
            min_y[0] = min(min_y[0], y_int)


for _ in range(inp()):
    solve()

if min_y[0] == float("inf"):
    print(-1.0)
else:
    print(min_y[0])
