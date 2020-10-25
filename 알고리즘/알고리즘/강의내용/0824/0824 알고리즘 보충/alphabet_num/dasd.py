import sys
sys.stdin = open('input.txt', 'r')

n = input()
c = list(n)

for i in c:
    print(ord(i)-64, end=" ")