import datetime

# Initialize a dictionary to store expenses by category
expenses = {}

# Function to input and categorize expenses
def record_expense():
    global expenses
    date = datetime.date.today()
    expense = float(input("Enter the expense amount: $"))
    category = input("Enter the expense category: ").strip().lower()

    # Check if the category already exists in the dictionary
    if category in expenses:
        expenses[category].append((date, expense))
    else:
        expenses[category] = [(date, expense)]

# Function to calculate total expenses
def calculate_total_expenses():
    total = 0
    for category, expense_list in expenses.items():
        for _, expense in expense_list:
            total += expense
    return total

# Function to display insights
def display_insights():
    total_expenses = calculate_total_expenses()
    print("\nExpense Insights:")
    print(f"Total Expenses: ${total_expenses:.2f}")

    # Calculate and display expenses by category
    for category, expense_list in expenses.items():
        category_total = sum(expense for _, expense in expense_list)
        category_percentage = (category_total / total_expenses) * 100
        print(f"{category.capitalize()} Expenses: ${category_total:.2f} ({category_percentage:.2f}%)")


while True:
    print("\nExpense Tracker Menu:")
    print("1. Record an Expense")
    print("2. Display Insights")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        record_expense()
    elif choice == '2':
        display_insights()
    elif choice == '3':
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
