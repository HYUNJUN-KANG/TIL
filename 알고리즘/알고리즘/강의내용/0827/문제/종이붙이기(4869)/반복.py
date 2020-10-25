import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input()) + 1):
    N = int(input()) // 10
    memo = [0] * (N+1)   # 초기값 0 >> 이 문제의 답을 아직 구하지 않음.

    memo[1], memo[2] = 1, 3    # 기저사레 저장

    for i in range(3, N + 1): # i -> 문제의 크기를 나타내는 값
        memo[i] = memo(i-1) + memo(i-2) * 2

    print(memo[N])