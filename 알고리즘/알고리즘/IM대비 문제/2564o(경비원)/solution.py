import sys
sys.stdin = open('input.txt', 'r')

def length(dir, len):
    if dir == 1:
        return len
    if dir == 2:
        return width + height + width - len
    if dir == 3:
        return 2*(width+height) - len
    if dir == 4:
        return width + len

width, height = map(int, input().split())

N = int(input())

shop = [list(map(int, input().split())) for _ in range(N)]

dg_dir, dg_len = map(int, input().split())
dg = length(dg_dir, dg_len)

result = 0

for i in range(len(shop)):
    shop_dir, shop_len = shop[i][0], shop[i][1]
    len = length(shop_dir, shop_len)
    result += min(abs(len - dg), square - abs(len-dg))

print(result)