def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def f(x):
    cnt = 0
    while x != 0:
        x //= 3
        cnt += 1
    return cnt

def main():
    n = inp()
    a = [0] * n

    
        

if __name__ == "__main__":
    main()




