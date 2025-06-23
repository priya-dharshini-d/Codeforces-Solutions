def main():
    n = int(input())
    a = list(map(int, input().split()))

    s = 0
    f = n - 1
    last = 0
    total = 0
    moves = []

    while True:
        if (a[f] < last and a[s] < last) or s > f:
            break

        if a[f] >= last and a[s] >= last:
            if a[f] < a[s]:
                last = a[f]
                total += 1
                moves.append('R')
                f -= 1
            else:
                last = a[s]
                total += 1
                moves.append('L')
                s += 1
        elif a[f] > last:
            last = a[f]
            total += 1
            moves.append('R')
            f -= 1
        elif a[s] > last:
            last = a[s]
            total += 1
            moves.append('L')
            s += 1
        else:
            break

    print(total)
    print(''.join(moves))


if __name__ == "__main__":
    main()
