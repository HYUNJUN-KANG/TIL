import sys
sys.stdin = open('input.txt', 'r')



def dfs(n, v):


    global cnt
    cnt = 0
    visited[n][v] = 1
    global result
    result = 0

    if n == 0:
        result = v
        return result, cnt

    for i in range(3):
        next_n = n + dr[i]
        next_v = v + dc[i]
        if 0 <= next_n < 100 and 0 <= next_v < 100 and li[next_n][next_v] == 1 and visited[next_n][next_v] != 1:
            cnt += 1
            return dfs(next_n, next_v)




for tc in range(1, 11):

    T = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]


    # 좌 우 아래
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    visited = [[0] * 100 for _ in range(100)]

    result = 0


    n = 99
    for i in range(99, -1, -1):
        if li[99][i] == 1:
            dfs(n, i)

        if cnt < min_cnt:
            min_cnt = cnt
            result = v


    print(result)



    #
    # print("#{} {}".format(tc, result))
