import random as rd

"""
投擲兩個骰子重複N次, 觀察兩點數相加和event的機率
"""

# basic version
N = int(input("Enter an integer(1): "))
event = int(input("Please enter the number 2~12: "))

if event > 12 or event < 2:
    print("========================")
    print("Please check the number!")
    print("========================")
    raise 

dice_1 = [i for i in range(1, 7)]
dice_2 = [i for i in range(1, 7)]
f = 0

for i in range(N):
    d1 = rd.choice(dice_1)
    d2 = rd.choice(dice_2)
    if d1 + d2 == event:
        f = f + 1
    else:
        continue

print(f"Probability of sum of {event}: {f/N: .4f}")
print("-" * 20)

# general version
N = int(input("Enter an integer(2): "))
dice_1 = [i for i in range(1, 7)]
dice_2 = [i for i in range(1, 7)]
result = []

for i in range(N):
    d1 = rd.choice(dice_1)
    d2 = rd.choice(dice_2)
    result.append(d1 + d2)

while True:
    event = int(input("Please enter the number 2~12: "))

    if event <= 12 and event >= 2:
        print(f"Probability of sum of {event}: {result.count(event)/N: .4f}")
    
    else:
        print("Please check the number!")
        break

print("-" * 20)

# general lite version
N = int(input("Enter an integer(3): "))
result = [rd.choice(range(1, 7)) + rd.choice(range(1, 7)) for _ in range(N)]

while True:
    event = int(input("Please enter the number 2~12: "))

    if event <= 12 and event >= 2:
        print(f"Probability of sum of {event}: {result.count(event)/N: .4f}")
    
    else:
        print("Please check the number!")
        break
