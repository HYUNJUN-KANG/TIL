import sys
sys.stdin = open('input.txt', 'r')



def dfs(n, v):
    global result
    visited[n][v] = 1

    if n == 0:
        result = v
        return result

    for i in range(3):
        next_n = n + dr[i]
        next_v = v + dc[i]
        if 0 <= next_n < 100 and 0 <= next_v < 100 and li[next_n][next_v] == 1 and visited[next_n][next_v] != 1:
            return dfs(next_n, next_v)


for tc in range(1, 11):

    T = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]

    n = 99
    v = li[99].index(2)

    # 좌 우 상
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    visited = [[0] * 100 for _ in range(100)]

    result = 0


    dfs(n, v)

    print("#{} {}".format(tc, result))



