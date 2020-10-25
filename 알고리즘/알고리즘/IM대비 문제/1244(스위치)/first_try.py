import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
arr = list(map(int, input().split()))
C = int(input())

for i in range(C):

    G, N = map(int, input().split())

    if G == 1:
        for i in range(N-1, len(arr), N):
            arr[i] = arr[i]^1

    else:
        N = N-1
        arr[N] = arr[N]^1
        for i in range(1, min(len(arr)-N, N+1)):
            if arr[N+i] == arr[N-i]:
                arr[N+i], arr[N-i] = arr[N-i]^1, arr[N+i]^1
            else:
                break

    print(arr[0], end=' ')
    for i in range(1, len(arr)):
        if i%20 == 0:
            print()
        print(arr[i], end=' ')
