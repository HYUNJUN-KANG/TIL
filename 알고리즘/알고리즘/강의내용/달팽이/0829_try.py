import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    li = [[0]*N for _ in range(N)]

    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    cnt = 1
    r = 0
    c = 0
    i = 0
    while cnt <= N * N:
        if 0 <= r < N and 0 <= c < N and li[r][c] == 0:
            li[r][c] = cnt
            cnt += 1
        else:
            r -= dr[i % 4]
            c -= dc[i % 4]
            i = (i + 1) % 4

        r += dr[i]
        c += dc[i]

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(li[i][j], end=' ')
        print()