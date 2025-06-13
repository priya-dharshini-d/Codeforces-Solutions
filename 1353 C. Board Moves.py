# 1353 C. Board Moves
def board_moves(t, test_cases):
    results = []
    for n in test_cases:
        ans = 0
        for i in range(1, n // 2 + 1):
            ans += 8 * i * i
        results.append(ans)
    return results


t = int(input())
test_cases = [int(input()) for _ in range(t)]

# Processing and Output
results = board_moves(t, test_cases)
for res in results:
    print(res)
