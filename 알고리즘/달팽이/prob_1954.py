import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    B = int(input())
    B_list = []

    for i in range(1, B*B+1):
        B_list.append(i)

    print(B_list)

    list_B = []

    for j in range(1, tc):


        for k in range(1, tc+1):
            tmp = []
            for q in range(1 + tc*(k-1), (k * tc) + 1):
                tmp.append(q)
            list_B.append(tmp)
    print(list_B)


    # for j in range(len(B_list)):
    #
    #     for k in range(len(B_list) // tc):
    #         if j < (len(B_list // tc)) + 1:
    #             D.append(j)
