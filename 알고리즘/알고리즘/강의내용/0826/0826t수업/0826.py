"1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
N = 7
en = 8
edges = list(map(int, input().split()))

# 인접행렬 작성하기 (adjacency matrix)
# 1번 노드에 1번 index에 집어넣을거니깐 N+1로 한다.

adj = [[0] * (N + 1) for _ in range(N + 1)]

# 시작 노드는 1번

for i in range(0, len(edges), 2):
    s = edges[i]  # start
    e = edges[i + 1]  # end
    adj[s][e] = 1  # s랑 e랑 연결
    adj[e][s] = 1  # e랑 s랑 연결

# 방문검사 배열이 필요: visited >> 노드의 길이 + 1
visited = [0] * (N + 1)
result = list()


# stack을 이용한 DFS

def dfs(v):
    stack = list()
    stack.append(v)
    visited[v] = 1  # 첫번째 노드는 방문했다.
    result.append(v)

    while stack:
        current = stack[-1]  # 가장 마지막에 있는 요소

        # 현재 노드에서 갈 수 있는 모든 노드 검사
        for i in range(len(adj[current])):
            # 현재 노드와 연결되어 있고 방문하지 않은 노드라면,
            if adj[current][i] == 1 and visited[i] == 0:
                stack.append(i)  # 다음 방문 추가
                visited[currnt] = 1
                result.append(current)
                break  # for 순서대로 방문하기 위하여.
            else:  # break에 걸리지 않음 = 현재 노드에서 갈 수 있는 노드 없음.
                stack.pop()

