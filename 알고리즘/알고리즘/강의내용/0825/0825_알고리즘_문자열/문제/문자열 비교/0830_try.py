import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    N = len(str2)
    M = len(str1)

    cnt = 0

    for i in range(N-M+1):
        for j in range(M):
            if str1[j] != str2[i+j]:
                break
        else:
            cnt = 1
            break

