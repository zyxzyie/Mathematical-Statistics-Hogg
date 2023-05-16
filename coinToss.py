import random as rd
import matplotlib.pyplot as plt

N = int(input("Enter an integer: "))

# For-Loop version
def for_loop_version(N: int):
    C = ["H", "T"]
    H, T = 0, 0

    for i in range(N):
        outcome = rd.choice(C)
        if outcome == "H": H = H + 1
        else: T = T + 1

    print(f"Probability of Head: {H/N: .4f}")
    print(f"Probability of Tail: {T/N: .4f}")


# List Comprehensions version
def list_compre_version(N: int):
    outcomes = ["H" if rd.choice(["H", "T"]) == "H" else "T" for _ in range(N)]
    print(f"Probability of Head: {outcomes.count('H')/N: .4f}")
    print(f"Probability of Tail: {outcomes.count('T')/N: .4f}")

list_compre_version(N)