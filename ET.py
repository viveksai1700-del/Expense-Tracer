import json
from datetime import datetime

FILE_NAME = "expenses.json"


# Load existing expenses
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save expenses
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add a transaction
def add_transaction(expenses):
    transaction_type = input("Enter type (income/expense): ").lower()

    if transaction_type not in ["income", "expense"]:
        print("❌ Invalid type!")
        return

    category = input("Enter category: ")
    amount = float(input("Enter amount: ₹"))
    description = input("Enter description: ")

    transaction = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "type": transaction_type,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(transaction)
    save_expenses(expenses)

    print("✅ Transaction added successfully!")


# View all transactions
def view_transactions(expenses):
    if not expenses:
        print("\n📭 No transactions found.")
        return

    print("\n========== TRANSACTIONS ==========")

    for i, transaction in enumerate(expenses, start=1):
        print(f"""
{i}. {transaction['date']}
   Type        : {transaction['type']}
   Category    : {transaction['category']}
   Amount      : ₹{transaction['amount']:.2f}
   Description : {transaction['description']}
""")


# Show financial summary
def show_summary(expenses):
    income = 0
    expense = 0

    for transaction in expenses:
        if transaction["type"] == "income":
            income += transaction["amount"]
        else:
            expense += transaction["amount"]

    balance = income - expense

    print("\n========== SUMMARY ==========")
    print(f"💰 Total Income  : ₹{income:.2f}")
    print(f"💸 Total Expense : ₹{expense:.2f}")
    print(f"💵 Balance       : ₹{balance:.2f}")


# Show expenses by category
def category_summary(expenses):
    categories = {}

    for transaction in expenses:
        if transaction["type"] == "expense":
            category = transaction["category"]

            if category not in categories:
                categories[category] = 0

            categories[category] += transaction["amount"]

    if not categories:
        print("\n📭 No expenses found.")
        return

    print("\n====== EXPENSES BY CATEGORY ======")

    for category, amount in categories.items():
        print(f"📌 {category}: ₹{amount:.2f}")


# Delete a transaction
def delete_transaction(expenses):
    view_transactions(expenses)

    if not expenses:
        return

    try:
        number = int(input("\nEnter transaction number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            save_expenses(expenses)

            print(
                f"🗑️ Deleted: "
                f"{deleted['category']} - ₹{deleted['amount']:.2f}"
            )
        else:
            print("❌ Invalid transaction number.")

    except ValueError:
        print("❌ Please enter a valid number.")


# Main program
def main():
    expenses = load_expenses()

    while True:
        print("""
====================================
        💰 EXPENSE TRACKER
====================================

1. Add Transaction
2. View Transactions
3. Show Summary
4. Category Summary
5. Delete Transaction
6. Exit

====================================
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction(expenses)

        elif choice == "2":
            view_transactions(expenses)

        elif choice == "3":
            show_summary(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            delete_transaction(expenses)

        elif choice == "6":
            print("\n👋 Thank you for using Expense Tracker!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()