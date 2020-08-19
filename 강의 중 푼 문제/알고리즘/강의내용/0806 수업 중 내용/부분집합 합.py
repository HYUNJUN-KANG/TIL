import sys
sys.stdin = open('input.txt', 'r')

N,K = map(int, input().split())       # N: 부분집합 원소 수
                                    # K: 부분집합의 합

arr = [i for i in range(1, 12+1)]
ans = 0

# 각각의 원소가 포함될지 안될지(1인지 0인지)를 비트랑 비교
# 결과가 0이 아니면 해당 비트가 부분집합에 포함된다.
# 부분집합의 모양을 판단


for bits in range(1, 1<<12):      # 전체 경우의 수
    cnt = S = 0
    for i in range(12):       # 0 ~ 11 인덱스에 해당하는 값 = i
        if bits & (1<<i):
            cnt += 1
            S += arr[i]

    if cnt == N and S == K:            # cnt 가 N자리가 됐을 때
        ans += 1
