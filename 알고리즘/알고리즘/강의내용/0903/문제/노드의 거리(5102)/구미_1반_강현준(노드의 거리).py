import sys
sys.stdin = open('input.txt', 'r')

def bfs(v):

    global result

    Q = []
    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.pop(0)
        for w in range(1, N+1):
            if G[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = 1
                distance[w] = distance[v] + 1
                if w == e:
                    result = distance[w]
                    return
    return
T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    G = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N + 1)
    distance = [0] * (N + 1)

    for i in range(M):
        r, c = map(int, input().split())
        G[r][c] = G[c][r] = 1


    s, e = map(int, input().split())

    result = 0
    bfs(s)

    print("#{} {}".format(tc, result))