# 1257D - Yet Another Monster Killing Problem

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        m = int(input())
        heroes = []
        for _ in range(m):
            p, s = map(int, input().split())
            heroes.append((s, p))

        # Preprocess: for each possible endurance, store the max power available
        max_power = [0] * (n + 2)
        for s, p in heroes:
            max_power[s] = max(max_power[s], p)

        # Optimize: propagate the maximum power backward
        for i in range(n, 0, -1):
            max_power[i] = max(max_power[i], max_power[i + 1])

        days = 0
        i = 0
        while i < n:
            curr_max = 0
            j = i
            while j < n:
                curr_max = max(curr_max, a[j])
                length = j - i + 1
                if max_power[length] < curr_max:
                    break
                j += 1
            if i == j:
                days = -1
                break
            days += 1
            i = j
        print(days)

if __name__ == "__main__":
    solve()
