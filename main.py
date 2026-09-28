import numpy as np

expenses = []

print("Personal Expense Analyzer")
print("-------------------------")

for i in range(5):
    expense = float(input(f"Enter expense {i + 1}: "))
    expenses.append(expense)

expenses_array = np.array(expenses)

total = np.sum(expenses_array)
average = np.mean(expenses_array)
highest = np.max(expenses_array)
lowest = np.min(expenses_array)

print()
print("Results")
print("-------")
print("Expenses:", expenses_array)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)