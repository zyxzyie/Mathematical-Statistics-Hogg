n = int(input("Please enter number 2~365: "))

# my version
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

ans = 1 - (factorial(365) / factorial(365-n)) / 365 ** n
print(f"Probability of at least 2 people have the same BD \n in {n} people: {ans: .7f}")

print("-" * 20)

# textbook version
def bday(n):
    result = 1
    for i in range(1, n):
        result = result * ((365-i)/365)
    return 1 - result
ans = bday(n)
print(f"Probability of at least 2 people have the same BD \n in {n} people: {ans: .7f}")