import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


for t in range(1, T+1):

    n = int(input())

    matrix = [list(map(int, input().split())) for _ in range(n)]
    area = []
    area_li = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:

                x = 0
                for k in range(j, n):
                    if matrix[i][k]:
                        x += 1
                    else:
                        break

                y = 0
                for k in range(i, n):
                    if matrix[k][j]:
                        y += 1
                    else:
                        break

                for k in range(i, i+y):
                    for l in range(j, j+x):
                        matrix[k][l] = 0

                area.append([y, x, y * x])

    N = len(area)

    for i in range(0, N-1):
        idx = i
        for j in range(i+1, N):
            if area[idx][2] > area[j][2]:
                idx = j
            elif area[idx][2] == area[j][2]:
                if area[idx][0] > area[j][0]:
                    idx = j
        area[i][2], area[idx][2] = area[idx][2], area[i][2]
        area[i][1], area[idx][1] = area[idx][1], area[i][1]
        area[i][0], area[idx][0] = area[idx][0], area[i][0]
    print(area)

    str_list = []

    for i in range(N):

        str_list.append(area[i][0])
        str_list.append(area[i][1])

    print(f'#{t} {N}', end = " ")



    print(*str_list)



