# Personal Expense Tracker

A Python-based personal expense tracking application that uses SQLite for data persistence and Pandas/Matplotlib for financial analysis and visualization.

The application allows users to record, view, edit, and delete expenses while providing spending summaries, monthly budget tracking, CSV export, and visual spending analysis.

## Features

* Add new expenses
* View all recorded expenses
* Edit existing expenses
* Delete expenses
* Calculate total and average spending
* Analyze spending by category
* Track monthly budgets
* Display remaining monthly budget
* Export expense data to CSV
* Generate spending-by-category charts
* Generate monthly spending trend charts
* Persistent data storage using SQLite

## Tech Stack

* **Python**
* **SQLite**
* **Pandas**
* **Matplotlib**
* **Git & GitHub**

## Project Structure

```text
personal-expense-tracker/
│
├── analytics.py          # Expense analysis and visualization
├── database.py           # SQLite database operations
├── main.py               # Application entry point and menu
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Ignored files and directories
```

## How It Works

The application follows a simple modular architecture:

```text
User
  │
  ▼
main.py
  │
  ├──────────────► database.py
  │                    │
  │                    ▼
  │                SQLite
  │
  └──────────────► analytics.py
                       │
                       ├── Pandas
                       └── Matplotlib
```

`main.py` handles user interaction and application flow.

`database.py` manages SQLite operations including creating, inserting, retrieving, updating, and deleting expenses.

`analytics.py` loads expense data into Pandas and performs calculations, CSV export, and visualization.

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd personal-expense-tracker
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python main.py
```

The SQLite database will be created automatically when the application starts.

## Example Workflow

```text
========== PERSONAL EXPENSE TRACKER ==========

1. Add Expense
2. View Expenses
3. Edit Expense
4. Delete Expense
5. Expense Summary
6. Monthly Budget
7. Export to CSV
8. Spending Chart
9. Monthly Spending Trend
10. Exit
```

Users can enter expenses such as:

```text
Date: 2026-09-07
Category: Food
Description: Grocery shopping
Amount: 85.50
```

The application then stores the information in the SQLite database and makes it available for analysis.

## Analytics

The application provides several financial insights, including:

### Expense Summary

* Total expenses
* Number of transactions
* Average expense
* Spending by category

### Monthly Budget

The application compares the current month's spending against a user-defined budget and reports whether spending is:

* Under budget
* Over budget

### Spending Visualization

Matplotlib is used to generate:

* Spending by category
* Monthly spending trends

## Data Storage

Expense records are stored locally using SQLite.

Each expense contains:

| Field       | Description               |
| ----------- | ------------------------- |
| ID          | Unique expense identifier |
| Date        | Expense date              |
| Category    | Expense category          |
| Description | Expense description       |
| Amount      | Expense amount            |

The database file is intentionally excluded from Git using `.gitignore`.

## Future Improvements

Potential improvements for future versions include:

* User authentication
* Recurring expense support
* Custom expense categories
* Budget persistence
* Advanced financial dashboards
* Spending alerts
* SQLite database migrations
* Unit and integration testing
* REST API
* Web-based interface
* Interactive Plotly dashboard

## Learning Objectives

This project demonstrates practical use of:

* Python application development
* Modular programming
* Functions and input validation
* CRUD operations
* SQLite databases
* Pandas data analysis
* Matplotlib visualization
* CSV data export
* Exception handling
* Git version control

## Author

**Gokul Krishna**

Master's Student — Computer Science, Information Systems

Interested in **Machine Learning, Data Science, Data Analytics, and AI Engineering**.
