import random as rd

N = int(input("Enter an integer: "))

# For-Loop version
C = ["H", "T"]
H, T = 0, 0

for i in range(N):
    outcome = rd.choice(C)
    if outcome == "H": H = H + 1
    else: T = T + 1

print(f"Probability of H: {H/N: .4f}")
print(f"Probability of T: {T/N: .4f}")
print("-" * 20)

# List Comprehensions version
outcomes = ["H" if rd.choice(["H", "T"]) == "H" else "T" for _ in range(N)]
print(f"Probability of H: {outcomes.count('H')/N: .4f}")
print(f"Probability of T: {outcomes.count('T')/N: .4f}")