import random as rd
import matplotlib.pyplot as plt

N = int(input("Enter an integer: "))

# For-Loop version
def for_loop_version(N: int, figure=False):
    C = ["H", "T"]
    H, T = 0, 0

    for i in range(N):
        outcome = rd.choice(C)
        if outcome == "H": H = H + 1
        else: T = T + 1

    print(f"Probability of Head: {H/N: .4f}")
    print(f"Probability of Tail: {T/N: .4f}")

    if figure == True:
        plt.figure(figsize=(5, 4))
        plt.pie([H/N, T/N], labels=["H", "T"], autopct="%1.2f%%",
                startangle=90)
        plt.axis("equal")
        plt.show()


# List Comprehensions version
def list_compre_version(N: int, figure=False):
    outcomes = ["H" if rd.choice(["H", "T"]) == "H" else "T" for _ in range(N)]
    prob_of_H = outcomes.count('H')/N
    prob_of_T = outcomes.count('T')/N
    print(f"Probability of Head: {prob_of_H: .4f}")
    print(f"Probability of Tail: {prob_of_T: .4f}")

    if figure == True:
        plt.figure(figsize=(5, 4))
        plt.pie([prob_of_H, prob_of_T], labels=["H", "T"], autopct="%1.2f%%",
                startangle=90)
        plt.axis("equal")
        plt.show()

# for_loop_version(N)
list_compre_version(N)