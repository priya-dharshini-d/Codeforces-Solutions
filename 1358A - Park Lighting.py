# 1358A - Park Lighting
import math

def park_lighting(t, test_cases):
    results = []
    for n, m in test_cases:
        total = (n * (m // 2))
        if m % 2:
            total += math.ceil(n / 2)
        results.append(total)
    return results

# Input Reading
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Processing and Output
results = park_lighting(t, test_cases)
for res in results:
    print(res)
