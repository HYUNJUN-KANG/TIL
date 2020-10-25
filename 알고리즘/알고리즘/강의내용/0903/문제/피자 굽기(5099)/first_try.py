import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    li_num = [i+1 for i in range(M)]

    Q = li[0:N]
    Q_num = li_num[0:N]
    Q_left = li[N:]
    Q_num_left = li_num[N:]

    while len(Q) != 1:
        Q[0] = Q[0] // 2
        if Q[0] // 2 == 0:
            Q.pop(0)
            Q_num.pop(0)

            if len(Q_left) > 0:
                Q.append(Q_left[0])
                Q_left.pop(0)
                Q_num.append(Q_num_left[0])
                Q_num_left.pop(0)

        else:
            Q.append(Q.pop(0))
            Q_num.append(Q_num.pop(0))

    print(Q_num[0])