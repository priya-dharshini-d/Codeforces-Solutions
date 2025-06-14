# 1255A - Changing Volume

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        diff = abs(a - b)
        ans = diff // 5
        diff %= 5
        ans += diff // 2
        diff %= 2
        ans += diff
        print(ans)

if __name__ == "__main__":
    main()
