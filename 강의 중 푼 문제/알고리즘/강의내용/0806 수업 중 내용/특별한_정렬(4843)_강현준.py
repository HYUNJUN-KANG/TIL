import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    num = int(input())
    num_li = list(map(int, input().split()))
    idx = 0

    for i in range(num):
        change = 0
        idx = 0
        if len(num_li[i:num]) % 2 == 0:
            max_li = num_li[i]
            for j in range(i, num):
                if num_li[j] >= max_li:
                    max_li = num_li[j]
                    idx = j
        elif len(num_li[i:num]) % 2 != 0:
            min_li = num_li[i]
            for j in range(i, num):
                if num_li[j] <= min_li:
                    min_li = num_li[j]
                    idx = j
        change = num_li[i]
        num_li[i] = num_li[idx]
        num_li[idx] = change

    print("#%d" % tc, end=" ")
    for i in range(10):
        print(num_li[i], end=" ")
    print()
    # for i in range(10):
    #     print(num_li[i])
