def main():
    t = int(input())
    
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))

        total_sum = sum(a)

        if total_sum <= s:
            print(0)
            continue

        mx = [0] * n
        sum_ = [0] * n

        mx[0] = a[0]
        sum_[0] = a[0]

        for i in range(1, n):
            mx[i] = max(mx[i - 1], a[i])
            sum_[i] = sum_[i - 1] + a[i]

        total = 0
        for i in range(n):
            if sum_[i] - mx[i] <= s:
                total = i

        extra = 0
        for i in range(n):
            if mx[total] == a[i]:
                extra = i + 1
                break

        print(extra)

if __name__ == "__main__":
    main()
