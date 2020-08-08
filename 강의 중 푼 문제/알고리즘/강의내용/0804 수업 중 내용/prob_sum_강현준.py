import sys
sys.stdin = open('input.txt', 'r')


T = int(input())



for tc in range(1, T+1):

    N = list(map(int, input().split( )))

    B = list(map(int, input().split( )))

    L = []

    for i in range(0, len(B)-(N[1])+1):

        sum = 0

        for p in range(i, N[1]+i):
            sum += B[p]

        L.append(sum)

    max_val = 0
    min_val = 100000000

    for j in L:
        if j > max_val:
            max_val = j

    for k in L:
        if k < min_val:
            min_val = k

    diff = max_val - min_val

    print(f'#{tc} {diff}')