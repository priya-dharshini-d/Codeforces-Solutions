#1017A. The Rank.py

n = int(input())
marks = []
position = 1

# Input Thomas's marks (first student)
thomas = sum(map(int, input().split()))
marks.append(thomas)

# Input rest of the students and compare totals
for _ in range(1, n):
    total = sum(map(int, input().split()))
    if total > thomas:
        position += 1

print(position)
