import sys
sys.stdin = open('input.txt', 'r')

def next(r, c):
    return 0 <= r < 100 and 0 <= c < 100 and li[r][c] == 1

def dfs(r, c):
    global cnt
    visited[r][c] = 1

    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]

        if next(nr, nc) and visited[nr][nc] == 0:
            cnt += 1
            return dfs(nr, nc)
    else:

        return cnt

T = 10
for tc in range(1, T+1):
    t = int(input())

    li = [list(map(int, input().split())) for _ in range(100)]


    # 좌 우 아래
    dr = [0, 0, 1]
    dc = [-1, 1, 0]


    result = 0
    min_distance = 99999
    for i in range(100):
        if li[0][i] == 1:
            r = 0
            c = i
            cnt = 0
            visited = [[0] * 100 for _ in range(100)]

            distance = dfs(r, c)
            if distance < min_distance:
                min_distance = distance
                result = i

    print(result)