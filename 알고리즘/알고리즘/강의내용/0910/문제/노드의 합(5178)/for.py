T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    K = [0] * (N+1)
    for _ in range(M):
        num, val = map(int, input().split())
        K[num] = val

    for i in range(N - M, 0, -1):
        K[i] = K[i*2]
        if i * 2 + 1 <= N:
            K[i] = K[i*2 + 1]

    print(K[L])