T = int(input())

for tc in range(1, T+1):

    N = int(input())

    numbers = list(map(int, input().split()))

    max_v = 1
    min_v = 1000000            # 문제에서 주어진 최대, 최솟값으로 max, min을 잡아준다.

    for i in range(N):
        if max_v < numbers[i]:
            max_v = numbers[i]
        if min_v < numbers[i]:
            min_v = numbers[i]

    print("#%d" % tc, max_v - min_v)
