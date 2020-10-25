headline = list(input())

for i in range(len(headline)):

    if 'a' <= headline[i] <= 'z':
        headline[i] = chr(ord(headline[i]-32))

print(''.join(headline))