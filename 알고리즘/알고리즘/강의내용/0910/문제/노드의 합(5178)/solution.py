T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    K = [0] * (N+1)
    for _ in range(M):
        num, val = map(int, input().split())
        K[num] = val

    def dfs(v):
        if v > N: return 0
        l = dfs(v*2)
        r = dfs(v*2 + 1)
        K[v] += l + r

        return K[v]

    dfs(1)
    print(K[L])