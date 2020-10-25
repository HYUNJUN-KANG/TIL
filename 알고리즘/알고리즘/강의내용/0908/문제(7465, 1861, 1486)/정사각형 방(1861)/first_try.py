import sys
sys.stdin = open('input.txt', 'r')

def dfs(r, c):
    global cnt
    cnt = 0
    Q = []
    Q.append((r, c))

    while Q:
        r, c = Q.pop()
        cnt += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if li[nr][nc] == li[r][c] + 1 and 0 <= nr < N and 0 <= nc < N:
                Q.append((nr, nc))
                break

        else:
            return cnt

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_cnt = 0
    start_point = ((N ** 2) + 1)

    for r in range(N):
        for c in range(N):
            max_value = li[r][c]
            dfs(r, c)

            if cnt > max_cnt:
                max_cnt = cnt
                start_point = max_cnt

            elif cnt == max_cnt:
                if max_value < start_point:
                    start_point = max_value
    print(start_point)

