#122 B. Lucky Substring

def main():
    s = input()
    four = 0
    seven = 0

    for i in s:
        if i == '4':
            four += 1
        elif i == '7':
            seven += 1

    if four == 0 and seven == 0:
        print(-1)
    elif four >= seven:
        print(4)
    else:
        print(7)

if __name__ == "__main__":
    main()
