import sys
sys.stdin = open('input.txt', 'r')

def dfs(N):
    global cnt
    cnt += 1
    for i in adj[N]:
        dfs(i)

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    tmp_li = list(map(int, input().split()))

    adj = [[] for _ in range(E+2)]
    for idx, i in enumerate(range(0, len(tmp_li), 2)):
        a = int(tmp_li[i])
        b = int(tmp_li[i+1])
        adj[a].append(b)

    cnt = 0
    dfs(N)

    print("#{} {}".format(tc, cnt))
