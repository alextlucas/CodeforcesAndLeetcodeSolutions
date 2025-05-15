def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

def solve(pref, cnt):

    l, r = invr()
    r += 1
    sum = pref[r] - pref[l]
    mn = cnt[l]

    print(sum + mn)

N = 200_007
pref = [0] * N
cnt = [0] * N

def main():
   
    for i in range(1, N - 1):
        cnt[i] = cnt[i//3] + 1
        pref[i+1] = pref[i] + cnt[i]


    for _ in range(inp()):
        solve(pref, cnt)

if __name__ == "__main__":
    main()



"""""""""
4
1 3
2 4
199999 200000
19 84
"""""""""


