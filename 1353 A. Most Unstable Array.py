# 1353 A. Most Unstable Array

def most_unstable_array(t, test_cases):
    results = []
    for n, m in test_cases:
        if n == 1:
            results.append(0)
        elif n == 2:
            results.append(m)
        else:
            results.append(2 * m)
    return results

# Input Reading
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Processing and Output
results = most_unstable_array(t, test_cases)
for res in results:
    print(res)
