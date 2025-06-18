def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        for i in range(n):
            row = ''
            for j in range(m):
                if i == 0 and j == 0:
                    row += 'W'
                else:
                    row += 'B'
            print(row)

# Run the function
solve()
