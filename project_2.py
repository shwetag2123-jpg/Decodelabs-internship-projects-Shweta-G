
def expense_tracker():
    expenses = {}
    while True:
        category = input("Enter an expense category (or type 'done' to finish): ")
        if category.lower() == 'done':
            break
        amount = input(f"Enter the amount for {category}: ")
        try:
            expenses[category] = expenses.get(category, 0) + float(amount)
        except ValueError:
            print("Please enter a valid number.")

    print("Your expenses are:")
    for category, amount in expenses.items():
        print(f"{category}: ₹{amount:.2f}")

    return expenses


def expense_calculator(expenses):
    try:
        total_expense = sum(expenses.values())
        print(f"Total expenses: ₹{total_expense:.2f}")
        
    except ValueError:
        print("Please enter a valid number.")
    
    
    
if __name__ == "__main__":
    expenses = expense_tracker()
    expense_calculator(expenses)


