import sys
sys.stdin = open('input.txt', 'r')


a = input()
c = []
for i in a:
    for j in i:
        b = j.upper()
        c.append(b)

d = "".join(c)
print(d)