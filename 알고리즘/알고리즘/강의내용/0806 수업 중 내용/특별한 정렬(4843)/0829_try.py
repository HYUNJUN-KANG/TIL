import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    li = list(map(int, input().split()))
    li2 = []
    new_li = []
    for i in range(len(li)):
        li2.append(li[i])

    for i in range(len(li)):
        if i % 2 == 0:
            new_li.append(max(li2))
            li2.remove(max(li2))
        elif i % 2 != 0:
            new_li.append(min(li2))
            li2.remove(min(li2))

    print("#{}".format(tc), end=" ")
    for i in range(10):
        print("{}".format(new_li[i]), end=" ")
    print()