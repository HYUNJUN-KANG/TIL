#  첫 번째 줄에는 테스트 케이스 개수 T
# T개의 테스트 케이스가 주어진다.

# input(): 문자열 한 줄을 입력받음. >> 문자열
# 문자열 -> 숫자로 변경해줘야함: int()

T = int(input())

for tc in range(1, T+1):

    N = int(input())


    board = [list(map(int, input().split()) for in range(N)]  # 이차원 배열 선언

    for row in board:
        print(row)

    print("#%d" %tc)