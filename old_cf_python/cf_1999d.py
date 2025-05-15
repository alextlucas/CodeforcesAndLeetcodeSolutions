def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))



def main():
    s, t = insr(), insr()

    r = 0
    for l in range(len(s)):
        if s[l] == "?":
            if r < len(t):
                s[l] = t[r]
                r += 1
            else:
                s[l] = "a"
        elif r < len(t) and s[l] == t[r]:
            r += 1
    if r >= len(t):
        print("YES")
        print("".join(s))
    else:
        print("NO")
   


if __name__ == "__main__":
    for _ in range(inp()):
        main()