import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    visited = [0] * (sum(li) + 1)

    Q = [0]

    for j in li:
        for k in range(len(Q)):
            if visited[Q[k] + j]:
                continue
            visited[Q[k] + j] = 1
            Q.append(Q[k] + j)

    print("#{} {}".format(tc, len(Q)))
