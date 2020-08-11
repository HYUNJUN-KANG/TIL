import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    a = list(map(int, input().split()))
    board_num = a[0]
    attack_num = a[1]

    board = [list(map(int, input().split())) for _ in range(board_num)]

    max_val = []

    for i in range(board_num-attack_num+1):
        for j in range(board_num-attack_num+1):
            kill = 0
            for k in range(i, i+attack_num):
                for p in range(j, j+attack_num):
                    kill += board[k][p]
            max_val.append(kill)

    max_value = 0
    for i in max_val:
        if i > max_value:
            max_value = i
    print("#%d" % tc, max_value)