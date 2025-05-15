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


def solve():
    n, k = invr()
    counts = defaultdict(int)

    for _ in range(k):
        b, c = invr()
        counts[b] += c
    
    sorted_counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)
    unique = len(sorted_counts)
    
    res = 0
    for i in range(n):
        if i >= unique:
            break
        res += sorted_counts[i][1]
    
    print(res)



for _ in range(inp()):
    solve()