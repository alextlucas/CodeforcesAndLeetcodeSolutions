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
    n = inp()
    nums = inlt()
    found = False
    for i in range(n - 1):
        diff = abs(nums[i] - nums[i + 1])
        if diff != 7 and diff != 5:
            found = True
            print("NO")
            break
    if not found:
        print("YES")


for _ in range(inp()):
    solve()
