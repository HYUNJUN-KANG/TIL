import sys
sys.stdin = open('input.txt', 'r')

T = 10

for t in range(1, T+1):

    tc = int(input())

    li = [list(map(int, input().split())) for _ in range(100)]

    max_num = [0]*4

    for r in range(100):
        row_sum = 0
        for c in range(100):
            row_sum += li[r][c]

        if max_num[0] < row_sum:
            max_num[0] = row_sum


    for c in range(100):
        col_sum = 0
        for r in range(100):
            col_sum += li[r][c]

        if max_num[1] < col_sum:
            max_num[1] = col_sum


    for r in range(100):
        for c in range(100):
            if r == c:
                max_num[2] += li[r][c]

    for r in range(100):
        for c in range(100):
            if r + c == 99:
                max_num[3] += li[r][c]
    result = max_num[0]
    for i in range(4):
        if result < max_num[i]:
            result = max_num[i]



    print("#{} {}".format(tc, result))