# Python equivalent of the C++ program
n = int(input())
p = list(map(int, input().split()))

for i in range(1, n + 1):
    mark = [True] * n
    current = i
    while mark[current - 1]:
        mark[current - 1] = False
        current = p[current - 1]
    print(current, end=' ')
print()
