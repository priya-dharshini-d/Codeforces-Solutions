def solve():
    test = int(input())
    for _ in range(test):
        n, k = map(int, input().split())
        s = input()
        cnt = [[0] * 26 for _ in range(k)]

        # Count characters by position modulo k
        for i in range(n):
            char_index = ord(s[i]) - ord('a')
            cnt[i % k][char_index] += 1

        res = 0
        for i in range(k // 2):
            max_freq = 0
            for j in range(26):
                max_freq = max(max_freq, cnt[i][j] + cnt[k - i - 1][j])
            total = sum(cnt[i]) + sum(cnt[k - i - 1])
            res += total - max_freq

        # If k is odd, handle the center separately
        if k % 2 == 1:
            center = k // 2
            max_freq = max(cnt[center])
            res += sum(cnt[center]) - max_freq

        print(res)

# Run the solve function
solve()
