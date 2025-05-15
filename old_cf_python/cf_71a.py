N = int(input())

for i in range(0, N):
    A = str(input())
    if len(A) > 10:
        print(A[0],end="")
        print(len(A) - 2,end="")
        print(A[len(A)-1])
    else:
        print(A)
        
        



