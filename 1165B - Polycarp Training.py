# Python equivalent of the given C++ program

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    cnt = 0
    track = 1

    for i in range(n):
        if a[i] >= track:
            track += 1
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
