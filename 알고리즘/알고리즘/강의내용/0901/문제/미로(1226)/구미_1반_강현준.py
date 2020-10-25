import sys
sys.stdin = open('input.txt', 'r')

def dfs(r, c):
    global result

    if li[r][c] == 3:
        result = 1
        return

    selected[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and (li[nr][nc] == 0 or li[nr][nc] == 3) and selected[nr][nc] != 1 :
            dfs(nr, nc)

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # li = [list(map(int, input().split())) for _ in range(N)]
    li = [[0] for _ in range(N)]

    for i in range(N):
        li1 = input()

        for j in range(N):
            li[i].append(int(li1[j]))


    for i in range(N):
        for j in range(N):
            if li[i][j] == 2:
                r = i
                c = j
            else:
                pass

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    selected = [[0]*N for _ in range(N)]
    result = 0

    dfs(r, c)

    print("#{} {}".format(tc, result))
