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

    x, y, z, k = invr()
    res = 0

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if k % (i * j): continue
            g = k // (i * j)
            if g > z: continue
            possibilities = (x - i + 1) * (y - j + 1) * (z - g + 1)
            res = max(res, possibilities)
    print(res)

for _ in range(inp()):
    solve()

