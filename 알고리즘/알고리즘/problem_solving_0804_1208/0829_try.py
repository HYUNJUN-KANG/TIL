import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):
    dump = int(input())

    li = list(map(int, input().split()))

    for _ in range(dump):
        max_li = max(li)
        max_index = li.index(max_li)

        min_li = min(li)
        min_index = li.index(min_li)

        li[max_index] -= 1
        li[min_index] += 1

    diff = max(li) - min(li)

    print("#{} {}".format(tc, diff))