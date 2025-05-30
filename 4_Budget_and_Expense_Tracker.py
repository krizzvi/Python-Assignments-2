import json
from datetime import datetime

data = {"income": [], "expenses": []}

def add_income():
    amt = float(input("Income amount: "))
    category = input("Category: ")
    data["income"].append({"amount": amt, "category": category, "date": str(datetime.now().date())})
    print("Income recorded.")

def add_expense():
    amt = float(input("Expense amount: "))
    category = input("Category: ")
    data["expenses"].append({"amount": amt, "category": category, "date": str(datetime.now().date())})
    print("Expense recorded.")

def summary():
    income_total = sum(i["amount"] for i in data["income"])
    expense_total = sum(e["amount"] for e in data["expenses"])
    print(f"Total Income: ${income_total:.2f}")
    print(f"Total Expenses: ${expense_total:.2f}")
    print(f"Balance: ${income_total - expense_total:.2f}")

def main():
    while True:
        print("\n--- Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            summary()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()