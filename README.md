# Expense_tracker
The Personal Expense Tracker is a simple yet powerful Python application that helps users manage and track their daily expenses. With an easy-to-use command-line interface, this application allows users to record income, track spending, and analyze their financial habits.

# Features:

**Add Expense**: 
Allows users to input various expenses with categories (e.g., food, transportation, entertainment).

**View Expenses:**
Displays a summary of all recorded expenses, showing details such as amount, date, and category.

**View Income:** 
Track incoming funds alongside expenses for a full financial picture.

**Persistent Storage:** 
All data is saved to a file, ensuring that records persist between sessions.

# Technologies Used:

**Python:**
The app is built entirely in Python, using basic data structures like dictionaries and lists.

**File Handling:** 
Expenses and income records are saved in a json file, allowing for easy retrieval and updates.

**Date Handling:**
Python's datetime module is used to record transaction dates and generate monthly summaries.

# How It Works:

**.** The application is controlled via the command line interface (CLI).

**.** Users can choose from various options to add expenses, income, or view financial summaries.

**.** All entries (expenses and income) are stored with categories and dates for organized tracking.

# Example Usage:

**1.**  **Add an Expense:**

    Please enter the amount: 50
    Please enter the category (e.g., food, transportation): food
    Please enter a description (optional): Dinner at a restaurant
    Expense added successfully.


**2.**  **View All Expenses:**

     Your Expenses:
    Date       | Amount | Category     | Description
    2025-01-19 | 50     | Food         | Dinner at a restaurant
    2025-01-20 | 20     | Transport    | Bus fare

# Future Enhancements:

**Categories:**
Allow users to customize and add their own categories for expenses.

**Graphical User Interface (GUI)**
Add a GUI using frameworks like Tkinter for a more user-friendly experience.
**Reports and Charts**
Generate visual charts and reports to help users better understand their spending habits.
**Budget Limits:**
Implement budget tracking, with alerts when users exceed their set monthly limits for various categories.
**Currency Support**
Add support for different currencies for international users.

# License:
This project is licensed under the MIT License - see the LICENSE file for details.
