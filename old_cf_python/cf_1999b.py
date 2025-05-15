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


for _ in range(N):
    res = 0
    a, b, c, d = invr()
    if (a > c and b >= d) or (a>= c and b > d):
        res += 2
    if (a >= d and b > c) or (a > d and b >= c):
        res += 2
    print(res)
    