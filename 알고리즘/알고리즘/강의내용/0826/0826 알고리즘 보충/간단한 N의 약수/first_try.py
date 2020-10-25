import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

li = []

for i in range(1, t+1):
    if t % i == 0:
        value = t // i
        li.append(value)
for i in range(len(li)):

    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]

for i in li:
    print(i, end=" ")