import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):

    li = [input() for _ in range(5)]
    str_li = ''
    max_length = 0

    for i in range(5):
        max_length = max(max_length, len(li[i]))

    for i in range(max_length):
        for j in range(5):
            if len(li[j]) > i:
                str_li += li[j][i]

    print("#{} {}".format(tc, str_li))