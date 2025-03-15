print("Simple Interest Calculator")

principal_amount = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate: "))
time = int(input("Enter Time: "))

interest_amount = (principal_amount * rate * time) / 100

print("Total Interest: " + str(interest_amount))