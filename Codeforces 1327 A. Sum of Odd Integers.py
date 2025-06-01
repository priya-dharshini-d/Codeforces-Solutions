# Problem name - A. Sum of Odd Integers
# Problem url - https://codeforces.com/contest/1327/problem/A

def can_represent_as_distinct_odds(n, k):
    return n >= k * k and n % 2 == k % 2

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        if can_represent_as_distinct_odds(n, k):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()





"""
✅ Condition 1: n >= k * k
📌 Why?

The smallest possible sum of k distinct positive odd numbers is: k² 

 
So, you can’t use k odd numbers to reach n if n < k² — it's mathematically impossible.

🧪 Example:
Try writing n = 5 as sum of k = 3 distinct odd numbers:

Minimum sum for 3 distinct odds = 
1+3+5=9

But 5 < 9 → not possible ❌

So, this condition ensures enough value to work with.

✅ Condition 2: n % 2 == k % 2

📌 Why?

The parity (even or odd) of the sum of odd numbers depends on how many odd numbers you add:

Odd count of odds → sum is odd

Even count of odds → sum is even

So:

If you're summing k odd numbers, the result will have the same parity as k

That means n must have the same parity as k

🧪 Example:

k = 2 → need to add 2 odd numbers → sum will be even (e.g., 1 + 3 = 4)

So n must be even too (e.g., n = 4 ✅, n = 5 ❌)

"""
