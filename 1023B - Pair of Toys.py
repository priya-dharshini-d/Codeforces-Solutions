# Python equivalent of the given C++ code

n, k = map(int, input().split())
total = k // 2

if k % 2 == 0:
    total -= 1

if k > (n + 1):
    total -= (k - n - 1)

if total <= 0:
    print(0)
else:
    print(total)
