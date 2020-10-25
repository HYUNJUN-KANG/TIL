import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    li = [0] * (len(str1))

    for j in range(len(str1)):
        for i in range(len(str2)):
            if str1[j] == str2[i]:
                li[j] += 1

    max_value = 0
    for i in li:
        if int(i) > max_value:
            max_value=int(i)

    print("#{} {}".format(tc, max_value))
