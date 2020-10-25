import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    li = list(map(int, input().split()))


    li_dict = {}

    for i in li:
        if i in li_dict:
            li_dict[i] += 1
        else:
            li_dict[i] = 1

    cnt_max = 0

    for key, value in li_dict.items():
        if cnt_max < value:
            cnt_max = value
            max_value = key
        elif cnt_max == value:
            if max_value < key:
                max_value = key

    print("#{} {}".format(num, max_value))