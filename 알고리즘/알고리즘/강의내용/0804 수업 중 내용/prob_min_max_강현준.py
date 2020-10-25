import sys
sys.stdin = open('input.txt', 'r')


T = int(input())


for tc in range(1, T+1):

    N = int(input())

    B = list(map(int, input().split()))

    max_1 = 0
    min_1 = 1000000
    for i in B:
        if i > max_1:

            max_1 = i

        if i < min_1:

            min_1 = i
    result = max_1 - min_1

    print(f'#{tc} {result}')
