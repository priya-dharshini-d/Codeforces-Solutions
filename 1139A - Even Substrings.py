def main():
    n = int(input())
    s = input()
    total = 0

    for i in range(n):
        num = int(s[i])
        if num % 2 == 0:
            total += i + 1

    print(total)

if __name__ == "__main__":
    main()
