import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T-1):
    temp = input()
    print(temp)
    year = temp[:4]
    month = temp[4:6]
    day = temp[6:]

    # flag = True
    # # 1 <= int(month) <= 12
    #
    # if int(month) <= 0 or int(month) >= 13:
    #     flag = False
    #
    # elif int(day) > day[int(month)] or int(day) <= 0:
    #     flag = False
    #
    # if flag:
    #     print("#{} {}/{}/{}".format(tc, year, month, day))
    # else:
    #     print("#{} -1".format(tc))
