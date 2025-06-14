# 1257B - Magic Stick

def main():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        if (x == 1 or x == 3) and y > x:
            print("NO")
        elif x == 2 and y > 3:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    main()
