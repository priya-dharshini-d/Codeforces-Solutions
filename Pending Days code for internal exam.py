# 1013 A. Piles With Stones
def main():
    n = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))

    increase = 0
    decrease = 0

    for i in range(n):
        if a2[i] > a1[i]:
            increase += a2[i] - a1[i]
        else:
            decrease += a1[i] - a2[i]

    if increase > decrease:
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    main()



  # 1016 A. Death Note

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    temp = 0
    for i in range(n):
        temp += a[i]
        cnt = 0
        if temp >= m:
            cnt = temp // m
            temp %= m
        print(cnt, end=' ')
    print()

if __name__ == "__main__":
    main()

# 1020 A. New Building for SIS

def main():
    num_towers, num_floors, min_accessible_floor, max_accessible_floor, num_queries = map(int, input().split())

    for _ in range(num_queries):
        source_tower, source_floor, dest_tower, dest_floor = map(int, input().split())
        total_steps = 0

        # If both rooms are in the same tower, only vertical movement is needed
        if source_tower == dest_tower:
            print(abs(source_floor - dest_floor))
            continue

        # Adjust source floor to be within accessible elevator range if it's outside
        if source_floor > max_accessible_floor:
            total_steps += source_floor - max_accessible_floor
            source_floor = max_accessible_floor
        elif source_floor < min_accessible_floor:
            total_steps += min_accessible_floor - source_floor
            source_floor = min_accessible_floor

        # Add steps to move horizontally between towers and then to the destination floor
        total_steps += abs(source_tower - dest_tower) + abs(source_floor - dest_floor)
        print(total_steps)

if __name__ == "__main__":
    main()

# 934A. A Compatible Pair
def main():
    num1, num2 = map(int, input().split())
    array = list(map(int, input().split()))
    
    array.sort()  # Sort the array to find second largest easily
    
    maximum = int(input())
    for _ in range(1, num2):
        temp = int(input())
        maximum = max(maximum, temp)

    # Multiply the second largest element in array with the maximum of the second group
    print(maximum * array[-2])

if __name__ == "__main__":
    main()



