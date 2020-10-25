import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]


    mid = N // 2
    s = mid
    e = mid
    sum = 0

    for i in range(N):
        for j in range(s, e+1, 1):
            sum += arr[i][j]
        if i < mid:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(sum)