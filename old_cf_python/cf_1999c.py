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
    n, s, m = invr()

    segs = [[0,0], [m,m]] + [inlt() for i in range(n)]
    segs.sort()
    for i in range(1, n+2):
        if segs[i][0] - segs[i - 1][1] >= s:
            print("YES")
            return
    print("NO")


def main():
    for _ in range(inp()):
        solve()
if __name__ == "__main__":
    main()






