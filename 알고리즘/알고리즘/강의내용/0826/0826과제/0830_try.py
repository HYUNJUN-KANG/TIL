import sys
sys.stdin = open('input.txt', 'r')

def next(r, c):
    return 0 <= r < 100 and 0 <= c < 100 and li[r][c] == 1

def dfs(r, c):
    global result
    visited[r][c] = 1

    if r == 0:
        result = c
        return result

    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]

        if next(nr, nc) and visited[nr][nc] != 1:
            return dfs(nr, nc)

T = 10

for tc in range(1, T+1):
    t = int(input())

    li = [list(map(int, input().split())) for _ in range(100)]

    r = 99
    c = li[99].index(2)

    visited = [[0]*100 for _ in range(100)]

    # 좌 우 상
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    result = 0

    dfs(r, c)

    print(result)

