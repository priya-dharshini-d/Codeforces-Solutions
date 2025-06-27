import math

def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        mx = 0
        diff = 0
        for _ in range(n):
            a, b = map(int, input().split())
            mx = max(mx, a)
            diff = max(diff, a - b)
        
        if diff <= 0 and x > mx:
            print(-1)
        else:
            if x <= mx:
                print(1)
            else:
                ans = math.ceil((x - mx) / diff) + 1
                print(ans)

if __name__ == "__main__":
    main()
