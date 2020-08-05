import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):

    N = input()
    li = []
    li_max = []

    for i in range(100):
        B = input().split()
        li.append(B)

    for j in range(len(li)):
        sum_li_1 = 0

        for k in range(len(li[j])):
            sum_li_1 += int(li[j][k])
        li_max.append(sum_li_1)


    for q in range(len(li[0])):
        sum_li_2 = 0

        for q_2 in range(len(li)):

            sum_li_2 += int(li[q_2][q])

        li_max.append(sum_li_2)


    sum_li_3 = 0
    for w in range(len(li)):


        for w_1 in range(len(li[0])):
            if w == w_1:
                sum_li_3 += int(li[w][w_1])
    li_max.append(sum_li_3)

    sum_li_4 = 0
    for p in range(len(li)-1, -1, -1):
        for p_1 in range(len(li[0])):
            if p + p_1 == 99:
                sum_li_4 += int(li[p][p_1])
    li_max.append(sum_li_4)

    max_li = 0
    for m in range(len(li_max)):
        if li_max[m] > max_li:
            max_li = li_max[m]
    print(f'#{tc} {max_li}')



