#1095A - Repeating Cipher
n = int(input())
s = input()

cnt = 1
i = 0
while i < n:
    print(s[i], end='')
    i += cnt
    cnt += 1

print()
