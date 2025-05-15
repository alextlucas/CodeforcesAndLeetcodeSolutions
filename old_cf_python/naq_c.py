def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

res = [0]
def solve():
    
    if inp() % 2 == 1:
        res[0] += 1

for _ in range(inp()):
    solve()


print(res[0])