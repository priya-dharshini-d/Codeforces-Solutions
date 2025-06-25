from itertools import combinations

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def is_segment(a, b, c):
    return a + b == c or a + c == b or b + c == a

def main():
    lengths = list(map(int, input().split()))
    
    if len(lengths) != 4:
        print("Please enter exactly 4 integers.")
        return

    lengths.sort()

    triangle = False
    segment = False

    for combo in combinations(lengths, 3):
        a, b, c = combo
        if is_triangle(a, b, c):
            triangle = True
        elif is_segment(a, b, c):
            segment = True

    if triangle:
        print("TRIANGLE")
    elif segment:
        print("SEGMENT")
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
