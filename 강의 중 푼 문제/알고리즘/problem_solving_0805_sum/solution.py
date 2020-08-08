import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):

    tn = int(input())
    numbers = [list(map(int, input().split())) for _ in range(100)]      # @@@@@@@@@@@이중배열 쉽게 만들어줌@@@@@@@@@@@@     # for 문에서 굳이 변수를 사용하지 않는다면, _ 로 비워두기.

    # 가로 합, 세로 합, 대각 합(위), 대각 합(아래)을 저장하는 배열
    max_number = [0]*4          # @@@@@@@@@@@@@@@@@@@@@4개짜리 리스트@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    # 가로합
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += numbers[i][j]
            #반복문 안에서는 합
            pass
        # 반복이 끝나면, 가로합의 최댓값 구하기 (이전 최대값과 비교)

        if max_number[0] < row_sum:             # @@@@@@@@@@@@@@@@@ 바로 들어가야하는 리스트 인덱스 자리에 넣어줌@@@@@@@@@@@@@@@@
            max_number[0] = row_sum

    for i in range(100):
        col_sum = 0

        for j in range(100):
            col_sum += numbers[j][i]
            pass

        if max_number[1] < col_sum:             # @@@@@@@@@@@@@@@@@ 바로 들어가야하는 리스트 인덱스 자리에 넣어줌@@@@@@@@@@@@@@@@
            max_number[1] = col_sum


    # 대각합 (상)
    for i in range(100):
        for j in range(100):
            if i+j == 99:
                max_number[2] += numbers[i][j]

    for i in range(100):
        for j in range(100):
            if i==j:
                max_number[3] += numbers[i][j]

    result = max_number[0]
    for i in range(len(max_number)):
        if result < max_number[i]:
            result = max_number[i]

    print("%d" %tc, result)