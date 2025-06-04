#  Problem name - 1426A. Floor Number
import math

def solve():
    n, x = map(int, input().split())
    if n <= 2:
        print(1)
        return
    ans = math.ceil((n - 2) / x) + 1
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
