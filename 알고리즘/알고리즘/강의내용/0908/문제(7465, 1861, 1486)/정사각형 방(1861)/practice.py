import sys
sys.stdin = open('input.txt', 'r')

def bfs(i, j):
    global max_length
    global room_num
    Q = list()
    Q.append((i, j))

    cnt = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while Q:
        cr, cc = Q.pop()
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if room[nr][nc] == room[cr][cc] + 1:
                    Q.append((nr, nc))
                    cnt += 1
                    break

    if cnt > max_length:
        max_length = cnt
        room_num = room[r][c]
    elif cnt == max_length:
        if room_num > room[r][c]:
            room_num = room[r][c]


T = int(input())

for tc in range(1, T+1):
    N = 2

    room = [list(map(int, input().split())) for i in range(N)]

    max_length = 0
    room_num = N*N
    for i in range(N):
        for j in range(N):
            dfs(i, j)