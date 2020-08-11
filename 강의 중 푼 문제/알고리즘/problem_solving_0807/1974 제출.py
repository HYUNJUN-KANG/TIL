import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for t in range(T):
    total = 0

    li = [list(map(int, input().split())) for i in range(9)]


    for i in range(len(li)):
        row_check_list = [0] * 10
        for j in range(len(li[i])):
            number = li[i][j]
            row_check_list[number] += 1

        cnt = 0
        for k in range(len(row_check_list)):
            if row_check_list[k] == 1:
                cnt += 1
        if cnt == 9:
            total += 1


    for i in range(len(li)):
        column_check_list = [0] * 10
        for j in range(len(li[i])):
            number = li[j][i]
            column_check_list[number] += 1

        cnt = 0
        for k in range(len(column_check_list)):
            if column_check_list[k] == 1:
                cnt += 1
        if cnt == 9:
            total += 1


    for i in range(len(li)//3):
        for j in range(len(li[i])//3):
            box_check_list = [0] * 10
            for m in range(3):
                for n in range(3):
                    number = li[(i*3)+m][(j*3)+n]
                    box_check_list[number] += 1
            cnt = 0
            for k in range(len(box_check_list)):
                if box_check_list[k] == 1:
                    cnt += 1
            if cnt == 9:
                total += 1


    if total == 27:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')