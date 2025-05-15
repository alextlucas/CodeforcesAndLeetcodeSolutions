def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def solve():
    maxTotal = 0
    n = inp()
    for x in range(2, n + 1):
        multi = 1
        total = 0
        while (multi * x) <= n:
            total += multi * x
            multi += 1
        if total > maxTotal:
            maxTotal = total
            res = x
            
    
    print(res)
        




for _ in range(inp()):
    solve()