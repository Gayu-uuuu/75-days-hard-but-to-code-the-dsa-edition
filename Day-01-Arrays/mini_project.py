expenses = [120, 300, 250, 100, 500]

if len(expenses) == 0:
    print("No expenses recorded")
else:
    max_expense = expenses[0]
    min_expense = expenses[0]
    total_expense = 0

    for expense in expenses:
        total_expense += expense   

        if expense < min_expense:
            min_expense = expense
        
        if expense > max_expense:
            max_expense = expense

    average_expense = total_expense / len(expenses)

    print("Maximum Expense:", max_expense)
    print("Minimum Expense:", min_expense)
    print("Total Expense:", total_expense)
    print("Average Expense:", average_expense)
