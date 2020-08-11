import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def searching(a, b):
    start = 1
    end = a
    cnt = 0

    while start < a:
        middle = (start + end) // 2
        cnt += 1
        if middle == b:
            return cnt
        elif middle > b:
            end = middle
        else:
            start = middle

    return cnt

for tc in range(1, T+1):

    page, page_a, page_b = map(int, input().split())

    page_list = []

    for i in range(1, page+1):
        page_list.append(i)

    count_a = searching(page, page_a)
    count_b = searching(page, page_b)

    if count_a > count_b:
        print("#%d B" % tc)
    if count_a < count_b:
        print("#%d A" % tc)
    if count_a == count_b:
        print("#%d 0" % tc)