# 거듭제곱: 밑수와 제곱수를 입력받아서 결과를 반환하는 함수작성
# 재귀 > 기저부(재귀가 호출되지 않는 가장 기본 단위) / 실행부 (연산을 해야하는 부분)

def power(base, exponent):
    if exponent == 0 or base == 0:
        return 1

    # exponent 제곱수가 짝수
    if exponent % 2 == 0:
        new_base = power(base, exponent//2)    # 절반 작업한 것을 두번 실행하여 전체를 구함.
        return new_base * new_base

    else:
        new_base = power(base, (exponent-1) // 2)
        return new_base * new_base


    # exponent 제곱수가 홀수