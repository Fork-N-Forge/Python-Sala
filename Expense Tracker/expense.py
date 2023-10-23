import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QFrame
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime

# Initialize a dictionary to store expenses by category
expenses = {}

class ExpenseTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 1200, 800)

        # Create a main widget to set as the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a main layout for the entire application
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a frame for the expense entry at the top
        entry_frame = QFrame()
        layout.addWidget(entry_frame)
        self.initExpenseEntryUI(entry_frame)

        # Add a horizontal separator line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        layout.addWidget(line)

        # Create a frame for the chart and visualization below the line
        chart_frame = QFrame()
        layout.addWidget(chart_frame)
        self.initChartUI(chart_frame)

        # Load expenses from the CSV file at the beginning
        self.load_expenses_from_csv()  # Moved to after it's defined
        # Display insights and pie chart
        self.display_insights()

    def load_expenses_from_csv(self):  # Define the function here
        if os.path.exists("expenses.csv"):
            df = pd.read_csv("expenses.csv")
            for index, row in df.iterrows():
                date = datetime.datetime.strptime(row["Date"], '%Y-%m-%d').date()
                category = row["Category"].strip().lower()
                expense = float(row["Expense"])

                if category in expenses:
                    expenses[category].append((date, expense))
                else:
                    expenses[category] = [(date, expense)]

    def initExpenseEntryUI(self, frame):
        layout = QVBoxLayout()
        frame.setLayout(layout)

        label_entry = QLabel("Here take expense entry")
        layout.addWidget(label_entry)

        # Create a horizontal layout for the expense entry section
        entry_layout = QHBoxLayout()
        layout.addLayout(entry_layout)

        label_amount = QLabel("Amount: ₹")
        entry_layout.addWidget(label_amount)

        self.entry_amount = QLineEdit()
        entry_layout.addWidget(self.entry_amount)

        label_category = QLabel("Category: ")
        entry_layout.addWidget(label_category)

        self.entry_category = QLineEdit()
        entry_layout.addWidget(self.entry_category)

        button_record = QPushButton("Record Expense")
        button_record.clicked.connect(self.record_expense)
        layout.addWidget(button_record)

    def initChartUI(self, frame):
        layout = QVBoxLayout()
        frame.setLayout(layout)

        self.insights_text = QTextEdit()
        self.insights_text.setReadOnly(True)
        layout.addWidget(self.insights_text)

        # Create a figure and canvas for the pie chart
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

    def record_expense(self):
        date = datetime.date.today()
        expense = float(self.entry_amount.text())
        category = self.entry_category.text().strip().lower()

        if category:
            if category in expenses:
                expenses[category].append((date, expense))
            else:
                expenses[category] = [(date, expense)]
            self.entry_amount.clear()
            self.entry_category.clear()
            self.display_insights()
            self.save_expenses_to_csv()

        
    def display_insights(self):
        total_expenses = self.calculate_total_expenses()
        self.insights_text.setPlainText("Expense Insights:\n")

        # Create a table to display insights
        table = QTableWidget()
        table.setColumnCount(2)  # Two columns for category and total expense
        table.setHorizontalHeaderLabels(["Category", "Total Expense"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Set alternating row colors and additional styling
        table.setStyleSheet("alternate-background-color: lightgray;")
        table.verticalHeader().setVisible(False)
        table.setSelectionBehavior(QTableWidget.SelectRows)
        table.setSelectionMode(QTableWidget.SingleSelection)
        table.setShowGrid(False)
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setFocusPolicy(Qt.NoFocus)

        # Populate the table with categories and total expenses
        for category, expense_list in expenses.items():
            total_category_expense = sum(expense for _, expense in expense_list)
            row_position = table.rowCount()
            table.insertRow(row_position)
            table.setItem(row_position, 0, QTableWidgetItem(category))
            table.setItem(row_position, 1, QTableWidgetItem(f"₹{total_category_expense:.2f}"))

        # Add a row for the overall total expense
        total_row_position = table.rowCount()
        table.insertRow(total_row_position)
        table.setItem(total_row_position, 0, QTableWidgetItem("Total"))
        table.setItem(total_row_position, 1, QTableWidgetItem(f"₹{total_expenses:.2f}"))

        # Add the table to the insights_text QTextEdit
        insights_layout = QVBoxLayout()
        insights_layout.addWidget(table)
        self.insights_text.setLayout(insights_layout)

        # Add the total expense to the QTextEdit
        self.insights_text.append(f"Total Expenses: ₹{total_expenses:.2f}")

        # Create or update the pie chart
        self.ax.clear()
        categories = list(expenses.keys())
        category_totals = [sum(expense for _, expense in expenses[cat]) for cat in categories]
        self.ax.pie(category_totals, labels=categories, autopct='%1.1f%%')
        self.ax.set_title('Expense Categories')
        self.canvas.draw()

    def calculate_total_expenses(self):
        total = 0
        for category, expense_list in expenses.items():
            for _, expense in expense_list:
                total += expense
        return total

    def save_expenses_to_csv(self):
        data = {"Date": [], "Category": [], "Expense": []}
        for category, expense_list in expenses.items():
            for date, expense in expense_list:
                data["Date"].append(date)
                data["Category"].append(category)
                data["Expense"].append(expense)

        df = pd.DataFrame(data)
        if not os.path.exists("expenses.csv"):
            df.to_csv("expenses.csv", index=False)
        else:
            df.to_csv("expenses.csv", mode="a", header=False, index=False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExpenseTrackerApp()
    ex.show()
    sys.exit(app.exec_())
