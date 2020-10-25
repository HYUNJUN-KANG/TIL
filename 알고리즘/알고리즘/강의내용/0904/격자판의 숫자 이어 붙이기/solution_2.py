import sys
sys.stdin = open('input.txt', 'r')

def numcase(i, j, num):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    num += box1[i][j]

    if len(num) == 7:
        result.add(num)
        return
    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if 0 <= nr < 4 and 0 <= nc < 4:
            numcase(nr, nc, num)


T = int(input())
for tc in range(1, T + 1):
    box1 = [list(input().split()) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            numcase(i, j, '')

    print('#{} {}'.format(tc, len(result)))