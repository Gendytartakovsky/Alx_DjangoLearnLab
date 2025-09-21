try:
    income = float(input("Enter your monthly income: "))
    expenses = float(input("Enter your monthly expenses: "))
    interest_rate = float(input("Enter annual interest rate (as a percentage, e.g., 5): "))
except ValueError:
    print("Please enter valid numbers for income, expenses, and interest rate.")
    exit()

# Calculate monthly savings
monthly_savings = income - expenses

if monthly_savings <= 0:
    print("You are not saving money monthly. Try to reduce expenses or increase income.")
    exit()

# Convert annual interest rate to monthly decimal rate
monthly_interest_rate = (interest_rate / 100) / 12

# Initialize total savings
total_savings = 0

# Compound monthly over 12 months
for month in range(1, 13):
    total_savings = (total_savings + monthly_savings) * (1 + monthly_interest_rate)

# Display results
print(f"\nYou save R{monthly_savings:.2f} per month.")
print(f"After 12 months with {interest_rate}% annual interest, you'll have: R{total_savings:.2f}")
