# 1252A - Copying Homework

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    for num in nums:
        print(n - num + 1, end=' ')
    print()

if __name__ == "__main__":
    main()
