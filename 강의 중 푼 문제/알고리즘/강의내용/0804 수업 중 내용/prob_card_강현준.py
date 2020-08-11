import sys
sys.stdin = open('input.txt', 'r')


T = int(input())



for tc in range(1, T+1):

    N = int(input())
    C = input()
    B = []

    for i in range(len(C)):

        B.append(C[i])

        F = list(map(int, B))

    D = {}

    for j in F:
        if j not in D.keys():
            D[j] = 1

        elif j in D.keys():
            D[j] += 1

    max_key = 0
    max_val = 0

    for key, val in D.items():
        if val > max_val:
            max_val = val
            max_key = int(key)

        elif val == max_val:
            if int(key) > max_key:
                max_key = int(key)

    print(f'#{tc} {max_key} {max_val}')













