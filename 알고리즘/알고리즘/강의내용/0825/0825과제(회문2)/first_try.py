import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, 11):
    n = input()

    result = 0

    li = []
    for k in range(100):
        li_data = input()
        li.append(li_data)

        for i in range(100, result, -1):
            if result > i:
                break
            for j in range(100 - i + 1):
                if li_data[j:i+j] == li_data[j:i+j][::-1]:
                    if len(li_data[j:i+j]) > result:
                        result = len(li_data[j:i+j])

    new_li = []
    new_li_value = ''

    for i in range(100):
        for j in li:
            new_li_value += j[i]
        new_li.append(new_li_value)
        new_li_value = ''

    for i in new_li:
        for j in range(100, result, -1):
            if result > j:
                break
            for k in range(100-j+1):
                if i[k:k+j] == i[k:k+j][::-1]:
                    if len(i[k:k+j]) > result:
                        result = len(i[k:k+j])

    print("#{} {}".format(tc, result))






