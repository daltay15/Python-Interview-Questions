expenses = [2200, 2350, 2600, 2130, 2190]

# In Feb how many dollars spent more than in Jan
difference = expenses[1] - expenses[0]
print("How much more spent in Feb compared to Jan: ", difference)

# Find out your total expenses in first quarter
print("Expenses in the first quarter: ",expenses[0] + expenses[1] + expenses[2])

# Find out if you spent exactly 2000 in any month
print("Spent $2,000 in any month? ", 2000 in expenses)

# June just finished and expenses are $1980, add to list
expenses.append(1980)
print(expenses)

# Got a refund of $200 in April, make the correction to the list
print("New expense for April: ", expenses[3] - 200)
