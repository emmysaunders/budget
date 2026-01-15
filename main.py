# main.py

# Lists to store incomes and expenses
income_list = []
expense_list = []

def show_menu():
    print("\n============================")
    print("    Student Budget Tracker   ")
    print("============================")
    print("1. Add income")
    print("2. Add expense")
    print("3. View summary")
    print("4. Exit")

def get_amount(entry_type):
    """
    General function to get a positive float from the user.
    entry_type: "income" or "expense" (for messages)
    """
    while True:
        amount = input(f"Enter {entry_type} amount: £")
        try:
            amount = float(amount)
            if amount <= 0:
                print(f"{entry_type.capitalize()} must be a positive number. Try again.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_income():
    """Add an income amount to the tracker."""
    amount = get_amount("income")
    income_list.append(amount)
    print(f"Income of £{amount:.2f} added successfully!")

def add_expense():
    """Add an expense amount to the tracker."""
    amount = get_amount("expense")
    expense_list.append(amount)
    print(f"Expense of £{amount:.2f} added successfully!")

def view_summary():
    """Display all incomes, expenses, totals, and balance."""
    print("\nBudget Summary")
    print("----------------------")
    
    if income_list:
        print("Income entries:")
        for i, amount in enumerate(income_list, 1):
            print(f"{i}. £{amount:.2f}")
    else:
        print("No income entries yet.")

    if expense_list:
        print("\nExpense entries:")
        for i, amount in enumerate(expense_list, 1):
            print(f"{i}. £{amount:.2f}")
    else:
        print("\nNo expense entries yet.")

    total_income = sum(income_list)
    total_expenses = sum(expense_list)
    balance = total_income - total_expenses

    print("\nTotals:")
    print(f"Total Income: £{total_income:.2f}")
    print(f"Total Expenses: £{total_expenses:.2f}")
    print(f"Balance: £{balance:.2f}")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_summary()
        elif choice == "4":  # polished exit
            print("\nThanks for using Student Budget Tracker! See you next time.\n")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
