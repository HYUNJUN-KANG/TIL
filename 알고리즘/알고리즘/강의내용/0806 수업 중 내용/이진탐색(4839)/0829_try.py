import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    total, target1, target2 = map(int, input().split())


    i = 1
    total1 = total
    center1 = int((total1 + i) / 2)
    c_page1 = center1
    cnt1 = 1

    while True:

        if target1 > c_page1:
            i = center1
            c_page1 = int((total1 + i)/2)
            center1 = c_page1
            cnt1 += 1
        elif target1 < c_page1:
            total1 = center1
            c_page1 = int((total1 + i)/2)
            center1 = c_page1
            cnt1 += 1
        elif target1 == c_page1:
            break
    i = 1
    total2 = total
    center2 = int((total2 + i) / 2)
    c_page2 = center2

    cnt2 = 1
    while True:

        if target2 > c_page2:
            i = center2
            c_page2 = int((total2 + i)/2)
            center2 = c_page2
            cnt2 += 1
        elif target2 < c_page2:
            total2 = center2
            c_page2 = int((total2 + i)/2)
            center2 = c_page2
            cnt2 += 1
        elif target2 == c_page2:
            break

    result = 0
    result_B = 'B'
    result_A = 'A'
    if cnt1 != cnt2:
        if cnt1 > cnt2:
            print("#{} {}".format(tc, result_B))
        elif cnt1 < cnt2:
            print("#{} {}".format(tc, result_A))

    elif cnt1 == cnt2:
        print("#{} {}".format(tc, result))

