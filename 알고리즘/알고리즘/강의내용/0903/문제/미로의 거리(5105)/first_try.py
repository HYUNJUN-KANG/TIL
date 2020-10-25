import sys
sys.stdin = open('input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    maze = [input() for _ in range(N)]
    sx = sy = ex = ey = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                sx, sy = i, j
            elif maze[i][j] == '3':
                ex, ey = i, j

    visited = [[0]*N for _ in range(N)]
    Q = [[sx, sy]]
    visited[sx][sy] = 1

    while Q:
        x, y = Q.pop(0)
        if x == ex and y == ey:
            break
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]

            if tx < 0 or tx == N or ty < 0 or ty == N: continue
            if maze[tx][ty] == '1' or visited[tx][ty]: continue
            visited[tx][ty] = visited[x][y] + 1
            Q.append([tx, ty])

    if visited[ex][ey]: visited[ex][ey] -= 2
    print(visited[ex][ey])