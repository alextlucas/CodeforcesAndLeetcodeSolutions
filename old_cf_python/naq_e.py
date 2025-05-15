from collections import defaultdict
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

res = []
counts = defaultdict(int)
n = inp()
for _ in range(10 * n):
    for x in inlt():
        counts[x] += 1

for k, v in counts.items():
    if v > (.2 * (10 * n)):
        res.append(k)


res.sort()
if len(res) == 0:
    print(-1)
else:   
    print(" ".join(map(str,res)))

