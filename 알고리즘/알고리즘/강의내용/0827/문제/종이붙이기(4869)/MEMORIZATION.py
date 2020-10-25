import sys
sys.stdin = open('input.txt', 'r')

def f(n):  # n: 문제의 크기(식별값) = 매개변수를 보고 판단
    # 기저 사례
    if n == 1: return 1
    if n == 2: return 3

    # 일반 사례
    if memo[n]: return memo[n]

    memo[n] = f(n-1) + f(n-2) * 2
    return memo[n]

for tc in range(1, int(input()) + 1):
    N = int(input()) // 10
    memo = [0] * (N+1)   # 초기값 0 >> 이 문제의 답을 아직 구하지 않음.
    print(f(N))