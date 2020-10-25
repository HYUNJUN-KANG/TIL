N = int(input())

li = list(map(int, input().split()))

cnt_p = 1 # 연속증가 길이
cnt_m = 1 # 연속감소 길이
max_cnt = 1  # 최대길이

for i in range(1, N):
    if li[i] > li[i-1]:            # 증가
        cnt_p += 1
        cnt_m = 1
    elif li[i] < li[i-1]:           # 감소
        cnt_m += 1
        cnt_p = 1
    elif li[i] == li[i-1]:          # 같을 때
        cnt_p += 1
        cnt_m ++ 1

    if max_cnt < cnt_p:
        max_cnt = cnt_p
    elif max_cnt < cnt_m:
        max_cnt = cnt_m