import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    li = input()
    result = []
    result_overlap = set()
    li_dict = {'S': 13, 'D': 13, 'H': 13, 'C': 13}

    for i in range(0, len(li), 3):
        li_2 = li[i:i+3]
        result.append(li_2)
        result_overlap.add(li_2)

    if len(result_overlap) != len(result):
        print("#{} ERROR".format(tc))

    else:
        for i in result:
            li_dict[i[0]] -= 1
        print("#{}".format(tc), end=' ')
        print(*li_dict.values())
