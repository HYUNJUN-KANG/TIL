import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    num = int(input())


    board = [[0]*10 for _ in range(10)]

    arr = []
    for i in range(num):
        co_list = list(map(int, input().split()))
        arr.append(co_list)

    for i in range(num):
        color = arr[i][4]
        if color == 1:
            for j in range(arr[i][0], arr[i][2]+1):
                for k in range(arr[i][1], arr[i][3]+1):
                    board[j][k] += 1


        if color == 2:
            for j in range(arr[i][0], arr[i][2]+1):
                for k in range(arr[i][1], arr[i][3]+1):
                    board[j][k] += 2

    cnt = 0

    for j in range(10):
        for k in range(10):

            if board[j][k] == 3:
                cnt += 1

    print("#%d" % tc, cnt)

