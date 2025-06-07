def calculateSimpleInterest(principalAmount: float, rate: float, time: int) -> float:
    return (principalAmount * rate * time) / 100

# 500.25 USD * 5% simple interest * 5 years
print(calculateSimpleInterest(500.25, 5, 5))
