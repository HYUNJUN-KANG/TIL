import sys
sys.stdin = open('input.txt', 'r')

def dfs(r, c, cnt, number):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    if cnt == 6:
        result.add(number)
        return

    for k in range(4):
        nr = i + dr[k]
        nc = i + dc[k]
        if 0 <= nr < 4 and 0 <= nc < 4:
            new_number = number + board[nr][nc]
            dfs(nr, nc, cnt+1, new_number)

T = int(input())

for tc in range(1, T+1):
    N = 4
    board = [list(input().split()) for _ in range(N)]
    result = set()

    for i in range(N):
        for j in range(N):
            dfs(i, j, 0, board[i][j])


    print(len(result))

