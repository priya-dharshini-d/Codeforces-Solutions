#Problem name - 1419A - Digit Game


def solve():
    n = int(input())
    s = input()

    odd1 = 0  # Count of odd digits at odd positions (0-indexed even positions)
    even = 0  # Count of even digits at even positions (0-indexed odd positions)

    for i in range(0, n, 2):
        d = int(s[i])
        if d % 2 == 1:
            odd1 += 1

    for i in range(1, n, 2):
        d = int(s[i])
        if d % 2 == 0:
            even += 1

    if n % 2 == 1:
        if odd1:
            print(1)
        else:
            print(2)
    else:
        if even:
            print(2)
        else:
            print(1)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()


"""

Game Summary:

Two players take turns removing digits from a number (represented as a string).

The first player (Player 1) plays on odd-numbered turns, and second player (Player 2) on even-numbered turns.

Whoever is the last to make a move wins, but only if the digit at that position satisfies a certain condition.

At the end of the game, the player who ends with a digit of their own parity wins:

Player 1 wins if the final digit is odd.

Player 2 wins if the final digit is even.

So the logic must figure out:

Who makes the last move.

Whether they can guarantee a win by ensuring the final digit is of their winning parity.

The Code:

if n % 2 == 1:
    # Player 1 makes the last move (since total moves are odd)
    if odd1:
        print(1)  # There's at least one odd digit at Player 1's positions → Player 1 can force a win
    else:
        print(2)  # No such odd digit → Player 1 cannot win → Player 2 wins
else:
    # Player 2 makes the last move (even number of digits)
    if even:
        print(2)  # There's at least one even digit at Player 2's positions → Player 2 can win
    else:
        print(1)  # No even digit at those positions → Player 1 wins
        
Definitions in Code:

odd1 counts odd digits at odd-numbered positions (0-based index even) — positions Player 1 can choose from.

even counts even digits at even-numbered positions (0-based index odd) — positions Player 2 can choose from.
"""
