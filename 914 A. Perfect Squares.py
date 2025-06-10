# 914 A. Perfect Squares

import math

def is_perfect_square(number):
    if number < 0:
        return False
    square_root = int(math.sqrt(number))
    return square_root * square_root == number

def main():
    array_size = int(input())
    numbers = list(map(int, input().split()))
    
    non_square_numbers = [num for num in numbers if not is_perfect_square(num)]
    non_square_numbers.sort()

    print(non_square_numbers[-1])  # Last element is the largest

if __name__ == "__main__":
    main()
