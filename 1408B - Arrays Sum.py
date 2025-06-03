# Problem name - 1408B - Arrays Sum 

import math

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    unique = 1
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            unique += 1

    if unique == 1:
        print(1)
        return

    if k == 1:
        if unique > 1:
            print(-1)
        return

    unique -= k
    ans = math.ceil(unique / (k - 1)) + 1
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
