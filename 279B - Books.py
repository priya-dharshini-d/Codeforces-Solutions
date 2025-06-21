def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    t = int(data[1])
    a = list(map(int, data[2:]))

    j = 0
    k = 0
    total = 0
    mx = 0

    while j < n:
        while k < n and total + a[k] <= t:
            total += a[k]
            k += 1
        mx = max(mx, k - j)
        total -= a[j]
        j += 1

    print(mx)

if __name__ == "__main__":
    main()
