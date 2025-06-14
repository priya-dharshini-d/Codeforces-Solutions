# 1257A - Two Rival Students

def main():
    t = int(input())
    for _ in range(t):
        n, x, a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        a1 = max(1, a - x)
        x -= (a - a1)
        b1 = min(b + x, n)
        # print(a1, b1)  # Uncomment to debug
        print(b1 - a1)

if __name__ == "__main__":
    main()
