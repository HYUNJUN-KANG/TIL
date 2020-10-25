import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, 11):
    n = input()

    result = 0

    li = []
    for k in range(100):
        li_data = input()
        li.append(li_data)


        for m in range(100, result, -1):
            if result > m:
                break
            for j in range(100 - m + 1):
                if li_data[j:j+m] == li_data[j:j+m][::-1]:
                    if len(li_data[j:j+m]) > result:
                        result = len(li_data[j:j+m])

    new_li = []
    new_li_value = ''
    for c in range(100):
        for r in li:
            new_li_value += r[c]
        new_li.append(new_li_value)
        new_li_value = ''

    for i in new_li:
        for m in range(100, result, -1):
            if result > m:
                break
            for k in range(100-m+1):
                if i[k:k+m] == i[k:k+m][::-1]:
                    if len(i[k:k+m]) > result:
                        result = len(i[k:k+m])

    print(result)