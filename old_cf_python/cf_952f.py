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
    
    def good(m):
        total = 0
        total += first
        for i in range(len(attacks)):
            total += attacks[i] * ((m - 1) // cooldown[i])
        return total >= h
    
    h, a = invr()
    attacks = inlt()
    cooldown = inlt()
    
    first = sum(attacks)
    
    l = 0
    r = 10 ** 12
    while l < r:
        m = (l + r) // 2
        if good(m):
            r = m
        else:
            l = m + 1
    
    print(l)
        
        
for _ in range(inp()):
    solve()

