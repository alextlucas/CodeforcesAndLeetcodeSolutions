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
    n = inp()
    arr = list(invr())
    
    res = 0
    maxEl = 0
    curTotal = 0
    for i in range(n):
        maxEl = max(maxEl, arr[i])
        curTotal += arr[i]
        if curTotal / 2 == maxEl:
            res += 1
        
    print(res)
    
for _ in range(inp()):
    solve()