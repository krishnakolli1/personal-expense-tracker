import sqlite3

import pandas as pd
import matplotlib.pyplot as plt
from database import get_monthly_total

DATABASE_NAME = "expenses.db"


def load_expenses():
    connection = sqlite3.connect(DATABASE_NAME)

    query = """
        SELECT *
        FROM expenses
        ORDER BY date
    """

    df = pd.read_sql_query(query, connection)

    connection.close()

    return df


def show_summary():
    df = load_expenses()

    if df.empty:
        print("\nNo expenses found.")
        return

    total = df["amount"].sum()

    print("\n========== EXPENSE SUMMARY ==========")
    print(f"Total expenses: ${total:.2f}")
    print(f"Number of expenses: {len(df)}")
    print(f"Average expense: ${df['amount'].mean():.2f}")

    print("\nSpending by category:")

    category_totals = df.groupby("category")["amount"].sum()

    for category, amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")


def export_to_csv():
    df = load_expenses()

    if df.empty:
        print("\nNo expenses available to export.")
        return

    filename = "expenses_export.csv"

    df.to_csv(filename, index=False)

    print(f"\nExpenses exported successfully to {filename}")


def create_category_chart():
    df = load_expenses()

    if df.empty:
        print("\nNo expenses available for chart.")
        return

    category_totals = df.groupby("category")["amount"].sum()

    category_totals.plot(
        kind="bar",
        title="Spending by Category"
    )

    plt.xlabel("Category")
    plt.ylabel("Amount ($)")

    plt.tight_layout()

    plt.savefig("spending_by_category.png")

    plt.show()
    
def show_monthly_budget(budget):
    today = pd.Timestamp.today()

    year = today.year
    month = today.month

    total_spent = get_monthly_total(year, month)

    remaining = budget - total_spent

    print("\n========== MONTHLY BUDGET ==========")
    print(f"Month: {year}-{month:02d}")
    print(f"Monthly Budget: ${budget:.2f}")
    print(f"Total Spent:    ${total_spent:.2f}")
    print(f"Remaining:      ${remaining:.2f}")

    if remaining >= 0:
        print("Status: UNDER BUDGET")
    else:
        print("Status: OVER BUDGET")
        
def create_monthly_trend_chart():
    df = load_expenses()

    if df.empty:
        print("\nNo expenses available for chart.")
        return

    df["date"] = pd.to_datetime(df["date"])

    monthly_totals = (
        df.groupby(df["date"].dt.to_period("M"))["amount"]
        .sum()
    )

    monthly_totals.index = monthly_totals.index.astype(str)

    monthly_totals.plot(
        kind="line",
        marker="o",
        title="Monthly Spending Trend"
    )

    plt.xlabel("Month")
    plt.ylabel("Amount ($)")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("monthly_spending_trend.png")

    plt.show()