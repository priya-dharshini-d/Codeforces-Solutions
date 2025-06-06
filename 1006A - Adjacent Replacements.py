#1006A - Adjacent Replacements

def mishkas_algorithm(n, a):
    result = []
    for num in a:
        if num % 2 == 0:
            result.append(num - 1)
        else:
            result.append(num)
    return result

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Process and output
res = mishkas_algorithm(n, a)
print(' '.join(map(str, res)))
