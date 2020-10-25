import sys
sys.stdin = open('input.txt', 'r')

def dfs(r, c):
    visited[r][c] = 1
    global cnt
    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr <= 99 and 0 <= nc <= 99 and data[nr][nc] == 1 and visited[nr][nc] == 0:
            cnt += 1
            return dfs(nr, nc)
    else:
        if r == 0:
            return cnt

T = 10
N = 100
for t in range(T):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 0, -1]
    dc = [1, -1, 0]

    li_result = []

    result = 0
    min_distance = 99999
    for i in range(N):
        if data[99][i] == 1:
            r = 99
            c = i
            cnt = 0
            visited = [[0]*N for _ in range(N)]

            distance = dfs(r, c)
            if distance <= min_distance:
                min_distance = distance
                result = i
                li_result.append(result)

    print(li_result)
    # print("#{} {}".format(tc, result))