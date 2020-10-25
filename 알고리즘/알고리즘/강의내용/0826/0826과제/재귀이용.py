import sys
sys.stdin = open('input.txt', 'r')

def check(x, y):
    if x < 0 or x >= 100 or y < 0 or y >= 100:
        return False
    if arr[x][y] == 0:
        return False
    return True

def ladder(x, y):
    if x == 0:
        global ans; ans = y
        return
    else:
        arr[x][y] = 0
        if check(x, y-1):
            ladder(x, y-1):
        elif check(x, y+1):
            ladder(x, y+1):
        else:
            ladder(x-1, y)

for tc in range(1, 11):
    case_num = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착점 찾기
    x = y = 0
    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break


    ans = 0
    ladder(x,y)


    print(y)