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
    a, b = input().split()
    a = list(a)
    b = list(b)

    a[0], b[0] = b[0], a[0]
    print("".join(a) + " " + "".join(b))
    

for _ in range(inp()):
    solve()