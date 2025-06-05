# 1405B - Array Cancellation

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    minus = 0
    cost = 0

    for i in reversed(range(n)):
        if a[i] < 0:
            minus -= a[i]  # accumulate absolute value of negative numbers
        else:
            if minus >= a[i]:
                minus -= a[i]
                a[i] = 0
            else:
                a[i] -= minus
                minus = 0
            cost += a[i]
    
    print(cost)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
