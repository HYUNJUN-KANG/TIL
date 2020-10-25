import sys
sys.stdin = open('input.txt', 'r')

def bfs(v):
    global result

    Q = []
    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.pop(0)
        for w in range(1, V+1):
            if li[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = 1
                distance[w] = distance[v] + 1
                if w == e:
                    result = distance[w]
                    return
    return
T = int(input())



for tc in range(1, T+1):
    V, E = map(int, input().split())

    li = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    distance = [0] * (V+1)

    for i in range(E):
        r, c = map(int, input().split())
        li[r][c] = 1
        li[c][r] = 1
    s, e = map(int, input().split())
    result = 1
    bfs(s)
    print(result)
