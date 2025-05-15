def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

expected = []
actual = []

n, m = invr()

for _ in range(n):
    expected.append(inp())

for _ in range(m):
    actual.append(inp())


diffs = []
for i in range(m):
    minDiff = float("inf")
    for j in range(n):
        minDiff = min(minDiff, abs(actual[i] - expected[j]))
    diffs.append(minDiff)

diffs.sort()
total = 0

for i in range(n):
    if i < m:
        if 0 <= diffs[i] <= 15:
            total += 7
        elif 15 < diffs[i] <= 23:
            total += 6
        elif 23 < diffs[i] <= 43:
            total += 4
        elif 43 < diffs[i] <= 102:
            total += 2

print(total)

"""l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        diff = abs(actual[i] - expected[m])
        if diff < minDiff:
            minDiff = diff
            r = m
        else:
            l = m + 1"""