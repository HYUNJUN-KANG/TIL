import sys
sys.stdin = open('input.txt', 'r')

def dfs(idx):
    if idx > N:
        return 0
    if Tree[idx]:
        return Tree[idx]
    left = idx * 2
    right = left + 1

    Tree[idx] = dfs(left) + dfs(right)

    return Tree[idx]

T = int(input())

for tc in range(1, T+1):

    N, M, L = map(int, input().split())

    Tree = [0 for _ in range(N+1)]

    for i in range(M):
        node, value = map(int, input().split())
        Tree[node] = value

    result = dfs(L)

    print("#{} {}".format(tc, result))