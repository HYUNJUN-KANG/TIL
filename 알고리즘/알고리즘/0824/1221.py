import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T):
    x,y = map(str, input().split())
    li = list(map(str, input().split()))

    li_dict = {
        "ZRO": 0,
        "ONE": 1,
        "TWO": 2,
        "THR": 3,
        "FOR": 4,
        "FIV": 5,
        "SIX": 6,
        "SVN": 7,
        "EGT": 8,
        "NIN": 9,
    }
    new_li = []
    for i in li:
        new_li += [li_dict[i]]
    new_li = sorted(new_li)

    result = []

    for key, value in li_dict.items():
        for i in new_li:
            if i == value:
                result += [key]
    result = " ".join(result)
    print("#{} {}".format(tc, result))


