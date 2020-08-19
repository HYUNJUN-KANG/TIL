import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    arr = [[0] * N for _ in range(N)]

    cnt = N * N

    # 우 하 좌 상

    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    r = 0
    c = 0
    d = 0

    num = 1

    while num <= cnt:
        if 0 <= r < N and 0 <= c < N and not arr[r][c]:
            arr[r][c] = num
            num += 1
        else:
            r -= dr[d]
            c -= dc[d]
            d = (d + 1) % 4

        r += dr[d]
        c += dc[d]

    for row in arr:
        print(row)