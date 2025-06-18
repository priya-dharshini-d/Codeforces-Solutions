#1332B - Composite Coloring
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        col = [0] * n
        cnt = 1

        # Use small primes as potential divisors
        for i in range(2, 1001):
            c = 0
            for j in range(n):
                if col[j] == 0 and a[j] % i == 0:
                    col[j] = cnt
                    c += 1
            if c:
                cnt += 1

        print(cnt - 1)
        print(" ".join(map(str, col)))

# Run the solve function
solve()
