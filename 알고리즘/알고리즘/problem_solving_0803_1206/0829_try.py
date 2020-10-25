import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):
    N = int(input())

    li = list(map(int, input().split()))

    cnt = 0

    for i in range(2, len(li)-2):

        max_value = max(li[i-2], li[i-1], li[i+1], li[i+2])

        if li[i] > max_value:
            value = li[i] - max_value

            cnt += value

        else:
            pass

    print("#{} {}".format(tc, cnt))