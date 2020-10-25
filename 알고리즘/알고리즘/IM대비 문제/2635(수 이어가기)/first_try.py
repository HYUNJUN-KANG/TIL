import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
max_l = -1
max_li = []

for i in range(1, 101):
    tmp = [N, i]   # 다음 숫자는 N-i [100, 99, 1
    while 1:
        next = tmp[-2]-tmp[-1]
        if next < 0:
            if len(tmp) > max_l:
                max_l = len(tmp)
                max_li = tmp
            break
        else:
            tmp.append(next)

print(max_l)
print(*max_li)