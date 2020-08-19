import sys
sys.stdin = open('input.txt.txt', 'r')

C, N = map(int, input().split())

li_li = [list(map(int, input().split())) for _ in range(N)]


for j in range(len(li_li)):
    for i in range(0, len(li_li)-1):
        a = li_li[i]
        b = li_li[i+1]

        if a[0] / a[1] > b[0] / b[1]:

            li_li[i], li_li[i+1] = li_li[i+1], li_li[i]



li_sum = []




for i in range(0, len(li_li)):
    a = li_li[i]

    if C % int(a[1]) == 0:
        li_sum.append((C / int(a[1]))*int(a[0]))
        C = 0
    elif C == 0:
        continue

    else:
        li_sum.append((C // int(a[1])) * int(a[0]))
        C = C % int(a[1])




print(int(sum(li_sum)))

# for i in range(N):
#     a = li_li[i]
#     x_value = a[0] / a[1]
#     li_value.append(x_value)
#
# li_sort = sorted(li_value)
# li_sum = []
# for i in range(li_sort):
#
#     if (i * C) % int(i * C) == 0:
#         li_sum.append(int((i * C)))
#         break


    # else:
    #     li_sum.append(int((i * C)))



# for i in range(N):
#     a = li_li[i]
#     # d = C % int(a[1])
#     price = a[0]
#
#     # if C % int(a[1]) == 0:
#     #     b = C // int(a[1])
#     #     price_value = int(price) * b
#     #     li_price.append(price_value)
#
#     if i == 0:
#         b = C // int(a[1])
#         price_value = int(price) * b
#         d = C % int(a[1])
#         li_price.append(price_value)
#
#     elif d != 0 and ((d % int(a[1])) == 0):
#         b = d // int(a[1])
#         price_value = int(price) * b
#
#         li_price.append(price_value)
#
#
#     # elif i == 0:
#     #     b = C // int(a[1])
#     #     price_value = int(price) * b
#     #     d = C % int(a[1])
#     #     li_price.append(price_value)
#
#     elif d != 0 and ((d % int(a[1])) != 0):
#         b = d // int(a[1])
#         price_value = int(price) * b
#
#         li_price.append(price_value)
#
#     else:
#
#         b = C // int(a[1])
#         price_value = int(price) * b
#
#         li_price.append(price_value)
#
#
# li_slice = li_price[0:N+1]
#
# print(sum(li_slice))



num = 456789
C = [0]*12

for i in range(6):
    C[num % 10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if C[i] >= 3:



