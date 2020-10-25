import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):



    li = [list(map(int, input().split())) for _ in range(9)]

    total_cnt = [0] * 3


    for r in range(9):
        li_cnt = [0] * 10
        row_cnt = 0
        for c in range(9):
            li_cnt[li[r][c]] += 1

        for i in range(10):
            if li_cnt[i] == 1:
                row_cnt += 1
        if row_cnt == 9:
            total_cnt[0] += 1

    for c in range(9):
        li_cnt = [0] * 10
        col_cnt = 0
        for r in range(9):
            li_cnt[li[r][c]] += 1

        for i in range(10):
            if li_cnt[i] == 1:
                col_cnt += 1
        if col_cnt == 9:
            total_cnt[1] += 1

    for i in range(0, 7, 3):
        for p in range(0, 7, 3):
            li_cnt = [0] * 10
            box_cnt = 0
            for r in range(i, i+3):
                for c in range(i, i+3):
                    li_cnt[li[r][c]] += 1
            for k in range(10):
                if li_cnt[k] == 1:
                    box_cnt += 1
            if box_cnt == 9:
                total_cnt[2] += 1

    result = 0
    for i in range(3):
        if total_cnt[i] == 9:
            result += 1

    if result == 3:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))