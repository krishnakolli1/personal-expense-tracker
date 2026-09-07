def edit_expense():
    print("\n========== EDIT EXPENSE ==========")

    try:
        expense_id = int(
            input("Enter expense ID to edit: ")
        )
    except ValueError:
        print("Please enter a valid ID.")
        return

    expenses = get_all_expenses()

    selected_expense = None

    for expense in expenses:
        if expense[0] == expense_id:
            selected_expense = expense
            break

    if selected_expense is None:
        print("\nExpense ID not found.")
        return

    print("\nCurrent expense:")

    print(f"Date: {selected_expense[1]}")
    print(f"Category: {selected_expense[2]}")
    print(f"Description: {selected_expense[3]}")
    print(f"Amount: ${selected_expense[4]:.2f}")

    print("\nEnter the new information.")

    date = input("Enter new date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    category = input("Enter new category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    description = input("Enter new description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    try:
        amount = float(
            input("Enter new amount: $")
        )

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    updated_rows = update_expense(
        expense_id,
        date,
        category,
        description,
        amount
    )

    if updated_rows > 0:
        print("\nExpense updated successfully!")
    else:
        print("\nExpense could not be updated.")
from datetime import datetime

from database import (
    create_database,
    add_expense,
    get_all_expenses,
    delete_expense,
    update_expense
)

from analytics import (
    show_summary,
    export_to_csv,
    create_category_chart,
    show_monthly_budget,
    create_monthly_trend_chart
)


def display_menu():
    print("\n===================================")
    print("       PERSONAL EXPENSE TRACKER")
    print("===================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Expense Summary")
    print("6. Monthly Budget")
    print("7. Export to CSV")
    print("8. Spending Chart")
    print("9. Monthly Spending Trend")
    print("10. Exit")
    print("===================================")


def add_new_expense():
    print("\n========== ADD EXPENSE ==========")

    date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        print("Please use YYYY-MM-DD.")
        return

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    description = input("Enter description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: $"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    add_expense(
        date,
        category,
        description,
        amount
    )

    print("\nExpense added successfully!")


def view_expenses():
    expenses = get_all_expenses()

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n================ EXPENSES ================")

    print(
        f"{'ID':<5}"
        f"{'Date':<15}"
        f"{'Category':<15}"
        f"{'Description':<25}"
        f"{'Amount':>10}"
    )

    print("-" * 70)

    for expense in expenses:

        expense_id, date, category, description, amount = expense

        print(
            f"{expense_id:<5}"
            f"{date:<15}"
            f"{category:<15}"
            f"{description:<25}"
            f"${amount:>9.2f}"
        )


def remove_expense():
    print("\n========== DELETE EXPENSE ==========")

    try:
        expense_id = int(
            input("Enter expense ID to delete: ")
        )
    except ValueError:
        print("Please enter a valid ID.")
        return

    deleted_rows = delete_expense(expense_id)

    if deleted_rows > 0:
        print("\nExpense deleted successfully!")
    else:
        print("\nExpense ID not found.")


def main():

    create_database()

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            edit_expense()

        elif choice == "4":
            remove_expense()

        elif choice == "5":
            show_summary()

        elif choice == "6":
            try:
                budget = float(input("Enter your monthly budget: $"))

                if budget <= 0:
                    print("Budget must be greater than zero.")
                else:
                    show_monthly_budget(budget)

            except ValueError:
                print("Please enter a valid budget.")

        elif choice == "7":
            export_to_csv()

        elif choice == "8":
            create_category_chart()
            
        elif choice == "9":
            create_monthly_trend_chart()

        elif choice == "10":
            print("\nThank you for using Personal Expense Tracker!")
        break

    else:
        print("\nInvalid choice. Please select 1-10.")


if __name__ == "__main__":
    main()