import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    # 노드 번호 = 1 ~ (E+1)
    # E = 간선의 수, E+1 = 노드의 수

    L = [0] * (E + 2)
    R = [0] * (E + 2)
    P = [0] * (E + 2)

    arr = list(map(int, input().split()))

    for i in range(0, E*2, 2):
        p, c = arr[i], arr[i+1]

        if L[p]: R[p] = c
        else: L[p] = c
        P[c] = p
    ans = 0
    def traverse(v):
        global ans
        if v == 0: return
        ans += 1
        traverse(L[v])
        traverse(R[v])

    traverse(N)
    print(ans)