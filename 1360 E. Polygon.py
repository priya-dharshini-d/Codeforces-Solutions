# 1360 E. Polygon

t = int(input())
for _ in range(t):
    n = int(input())
    poly = [input().strip() for _ in range(n)]
    
    check = True
    for i in range(n - 1):
        for j in range(n - 1):
            if poly[i][j] == '1' and poly[i + 1][j] == '0' and poly[i][j + 1] == '0':
                check = False
                break
        if not check:
            break

    print("YES" if check else "NO")
