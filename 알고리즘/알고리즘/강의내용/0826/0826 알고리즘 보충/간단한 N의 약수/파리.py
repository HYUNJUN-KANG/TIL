def attack(r, c):
    sum = 0

    for i in range(r, r+M):
        for j in range(c, c+M):

    return sum



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    fly = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N-M+1):       # 가로
        for j in range(N-M+1):       # 세로

            # 탐색을 위해서 2중 for 문
            tmp = attack(i, j)