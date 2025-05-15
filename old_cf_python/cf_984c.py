
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
    hits = set()
    target = ["1", "1", "0", "0"]
    s = insr()
    for i in range(len(s) - 3):
        if s[i:i+4] == target:
            hits.add(i)
            
    q = inp()
    for _ in range(q):
        idx, v = inlt()
        idx -= 1
        
        s[idx] = str(v)
        for i in range(max(0, idx - 3), min(len(s) - 3, idx + 3) + 1):
            if s[i:i+4] == target:
                hits.discard(i)

        for i in range(max(0, idx - 3), min(len(s) - 3, idx + 3) + 1):
            if s[i:i+4] == target:
                hits.add(i)
        
        if len(hits):
            print("YES")
        else:
            print("NO")
            
                


for _ in range(inp()):
    solve()