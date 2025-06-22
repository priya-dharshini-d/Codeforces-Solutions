def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ones = 0
    check = False

    for i in range(n):
        if not check and a[i] == 1 and i < n - 1:
            ones += 1
        if a[i] != 1:
            check = True

    if ones % 2 == 0:
        print("First")
    else:
        print("Second")


t = int(input())
for _ in range(t):
    solve()
