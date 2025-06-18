def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        has_one = False
        has_minus_one = False
        possible = True

        for i in range(n):
            if b[i] > a[i] and not has_one:
                possible = False
            elif b[i] < a[i] and not has_minus_one:
                possible = False
            
            # Update flags
            if a[i] == 1:
                has_one = True
            elif a[i] == -1:
                has_minus_one = True

        print("YES" if possible else "NO")

# Run the function
solve()
