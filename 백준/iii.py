import sys
sys.stdin = open("input.txt", 'r')



T = int(input())

b = []

for i in range(T):
    a = int(input())

    b.append(a)

    if a == 0:
        b = b[0:-2]

    print(b)


