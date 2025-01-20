import os
import json

# File to store expenses
data_file = "expenses.json"

# Load existing expenses or initialize new
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        expenses = json.load(file)
else:
    expenses = []

def save_expenses():
    """Save expenses to a file."""
    with open(data_file, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    """Add a new expense."""
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport): ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a description (optional): ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description,
    }
    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")

def view_expenses():
    """View all expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nYour Expenses:")
    print("=" * 50)
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['date']} | {expense['category']} | {expense['amount']} | {expense.get('description', '')}")
    print("=" * 50)

def delete_expense():
    """Delete an expense by its number."""
    view_expenses()

    if not expenses:
        return

    try:
        idx = int(input("Enter the expense number to delete: ")) - 1
        if 0 <= idx < len(expenses):
            removed = expenses.pop(idx)
            save_expenses()
            print(f"Deleted expense: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main program loop."""
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()