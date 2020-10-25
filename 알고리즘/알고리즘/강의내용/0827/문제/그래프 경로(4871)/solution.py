import sys
sys.stdin = open('input.txt', 'r')

# 함수가 처리되는 모든 부분에서 return 해줘야함.

def DFS(v):
    visit[v] = 1
    if v == e:
        return 1
    for w in range(1, V+1):
        if G[v][w] == 1 and visit[w] == 0:
            if DFS(w) == 1:
                return 1
    return 0

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    # 인접행렬, 정점의 번호 1~V
    G = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):   # 간선정보 읽기
        u, v = map(int, input().split())
        G[u][v] = 1     # 유향그래프이므로 반대는 표시하지 않는다!!!

    s, e = map(int, input().split())

    visit = [0] * (V+1)

    DFS(s)
