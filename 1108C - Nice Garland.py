def main():
    n = int(input().strip())
    s = input().strip()
    patterns = ["RGB", "RBG", "BRG", "BGR", "GBR", "GRB"]
    costs = [0] * 6
 
    # Calculate mismatches for each pattern
    for i in range(6):
        track = 0
        for j in range(n):
            if s[j] != patterns[i][track]:
                costs[i] += 1
            track += 1
            if (j + 1) % 3 == 0:
                track = 0
 
    # Find minimum mismatch index
    minn = 0
    for i in range(1, 6):
        if costs[i] < costs[minn]:
            minn = i
 
    # Print minimum cost
    print(costs[minn])
 
    # Construct and print final string
    result = (patterns[minn] * (n // 3)) + patterns[minn][:n % 3]
    print(result)
 
 
if __name__ == "__main__":
    main()
