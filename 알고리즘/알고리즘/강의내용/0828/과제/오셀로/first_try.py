import sys
sys.stdin = open('input.txt', 'r')

def dfs(r, c, t):
    board[r][c] = t
    # global cnt_b, cnt_w
    # cnt_b = 0
    # cnt_w = 0


    for i in range(8):
        r = r1
        c = c1
        t = t1
        while True:
            if 0 < r <= N and 0 < c <= N:
                board[r][c] += t

                if board[r][c] % 2 == 0:
                    for i in range(N + 1):
                        for j in range(N + 1):
                            if board[i][j] == 3:
                                if t == 1:
                                    board[i][j] = t
                                else:
                                    board[i][j] = t

                            else:
                                pass
                    break
                else:
                    pass

                r += dr[i]
                c += dc[i]

            else:
                break
    # return cnt_b, cnt_w
    # for r in range(N+1):
    #     for c in range(N+1):
    #         if board[r][c] == 3:
    #             board[r][c] = t

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    board = [[0] * (N+1) for _ in range(N+1)]

    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    nr = N // 2
    nc = N // 2

    board[nr][nc] = 2
    board[nr][nc+1] = 1
    board[nr+1][nc] = 1
    board[nr+1][nc+1] = 2

    # cnt_b = 0
    # cnt_w = 0

    for _ in range(M):
        r, c, t = map(int, input().split())
        r1 = r
        c1 = c
        t1 = t
        dfs(r, c, t)

    cnt_b = 0
    cnt_w = 0

    for r in range(N+1):
        for c in range(N+1):
            if board[r][c] == 1:
                cnt_b += 1
            elif board[r][c] == 2:
                cnt_w += 1

            else:
                pass

    print(cnt_b, cnt_w)
    # for i in range(N):
    #     nr = N // 2
    #     nc = N // 2
    #
    #     while True:
    #         if 0 < nr <= N and 0 < nc <= N:
    #             board[nr][nc] = 1
    #             nr += dr[i]
    #             nc += dc[i]
    #
    #         else:
    #             break
    # print(board)