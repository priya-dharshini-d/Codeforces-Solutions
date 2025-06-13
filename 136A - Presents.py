# 136A - Presents

n = int(input())
store = [0] * (n + 1)  # To match 1-based indexing

friend_list = list(map(int, input().split()))
for i in range(n):
    friendd = friend_list[i]
    store[friendd] = i + 1

# Output from 1 to n
print(' '.join(str(store[i]) for i in range(1, n + 1)))
