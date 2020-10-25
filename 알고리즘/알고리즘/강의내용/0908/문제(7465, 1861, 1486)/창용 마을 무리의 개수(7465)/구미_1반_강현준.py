import sys
sys.stdin = open('input.txt', 'r')

def bfs(v):
    selected[v] = 1
    Q.append(v)

    while Q:
        k = Q.pop(0)
        for c in range(1, N+1):
            if li[k][c] == 1:
                nc = c
                if selected[nc] != 1:
                    selected[nc] = 1
                    Q.append(nc)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [[0]*(N+1) for _ in range(N+1)]
    selected = [0]*(N+1)

    for i in range(M):
        r, c = map(int, input().split())
        li[r][c] = 1
        li[c][r] = 1
    Q = []
    cnt = 0
    for i in range(1, N+1):
        if selected[i] != 1:
            cnt += 1
            bfs(i)

    print("#{} {}".format(tc, cnt))
