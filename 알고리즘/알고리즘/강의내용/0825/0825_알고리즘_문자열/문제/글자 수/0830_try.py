import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    used_arr = [0]*26
    cnt_arr = [0]*26

    for c in str1:
        used_arr[ord[c]-ord("A")] = 1

    for c in str2:
        if used_arr[ord[c]-ord("A")] == 1:
            cnt_arr[ord(c)-ord("A")] += 1
