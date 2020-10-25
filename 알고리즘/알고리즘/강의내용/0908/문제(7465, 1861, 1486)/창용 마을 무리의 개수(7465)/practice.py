import sys
sys.stdin = open('input.txt', 'r')

def bfs(v):
    visited[v] = 1
    q.append(v)
    while q:
        a = q.pop(0)

        for j in li[a]:
            if not visited[j]:
                visited[j] = 1
                q.append(j)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [[0]*(N+1) for _ in range(N+1)]
    print(N, M)
    visited = [0]*(N+1)

    for i in range(M):
        s, e = map(int, input().split())
        li[s][e] = li[e][s] = 1
    q = []
    cnt = 0

    for n in range(1, N+1):
        if not visited[n]:
            cnt += 1
            bfs(n)

    print(cnt)