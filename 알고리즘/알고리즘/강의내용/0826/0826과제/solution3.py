import sys
sys.stdin = open('input.txt', 'r')

def check(x, y):
    if x < 0 or x >= 100 or y < 0 or y >= 100:
        return False
    if arr[x][y] == 0:
        return False
    return True

for tc in range(1, 11):
    case_num = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착점 찾기
    x = y = 0
    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break


    while x:           # x != 0 까지
        # 왼쪽으로 가는 경우
        if check(x, y-1):     # 갈 수 있다면
            while check(x, y-1):    # 갈 수 있을 때 까지 왼쪽으로
                y -= 1
        # 오른쪽으로 가는 경우
        elif check(x, y+1):
            while check(x, y+1):
                y += 1
        # 그 외, 위로 가는 경우
        x -= 1

    print(y)