import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):


    arr = [list(map(int, input().split())) for _ in range(T)]

    cnt = 0

    for i in range(len(arr)-1):
        sum_li = []

        for j in range(len(arr[0])):
            arr_int = int(arr[i][j])
            sum_li.append(arr_int)

        t = 1
        for k in sum_li:
            t = k * t

        if t == 362880:
            cnt += 1

    cnt_1 = 0
    for i in range(len(arr) - 1):
        sum_li_2 = []

        for j in range(len(arr[0])):
            arr_int = int(arr[j][i])
            sum_li_2.append(arr_int)

        p = 1
        for k in sum_li:
            p = k * p

        if p == 362880:
            cnt_1 += 1


    for i in range(len(arr) // 3):
        for j in range(len(arr[i]) // 3):
            box_check_list = [0] * 10
            for m in range(3):
                for n in range(3):
                    number = arr[(i * 3) + m][(j * 3) + n]
                    box_check_list[number] += 1
            cnt = 0
            for k in range(len(box_check_list)):
                if box_check_list[k] == 1:
                    cnt += 1
            print(cnt)

    # for i in range(len(arr)//3):
    #     sum_li_3 = []
    #     for j in range(len(arr)//3):
    #         for m in range(3):
    #             for n in range(3):
    #
    #                 arr_int = int(arr[(i*3) + m][(j*3) + n])
    #                 sum_li_3.append(arr_int)
    #
    #     cnt_2 = 1
    #
    #     q = 1
    #     for k in sum_li_3:
    #         q = k * q
    #
    #     if q == 362880:
    #         cnt_2 += 1
    #
    #     print(cnt_2)