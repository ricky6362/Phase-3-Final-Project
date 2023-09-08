import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Category, Expense, User

# Create SQLite database and tables
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Category '{name}' added successfully.")

def add_expense(description, amount, category_name, username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        category = session.query(Category).filter_by(name=category_name).first()
        if category:
            expense = Expense(description=description, amount=amount, category=category, user=user)
            session.add(expense)
            session.commit()
            print("Expense added successfully.")
        else:
            print(f"Category '{category_name}' does not exist.")
    else:
        print(f"User '{username}' does not exist. Please enter a valid username.")

def list_expenses():
    expenses = session.query(Expense).all()
    if expenses:
        for expense in expenses:
            print(f"ID: {expense.id}, Description: {expense.description}, Amount: {expense.amount}, Category: {expense.category.name}, User: {expense.user.username}")
    else:
        print("No expenses recorded.")

def remove_expense(expense_id):
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        session.delete(expense)
        session.commit()
        print(f"Expense ID {expense_id} removed successfully.")
    else:
        print(f"Expense ID {expense_id} not found.")

def add_user(username):
    user = User(username=username)
    session.add(user)
    session.commit()
    print(f"User '{username}' added successfully.")

def remove_user(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User '{username}' removed successfully.")
    else:
        print(f"User '{username}' not found.")

def add_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Category '{name}' added successfully.")

def remove_category(category_name):
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        session.delete(category)
        session.commit()
        print(f"Category '{category_name}' removed successfully.")
    else:
        print(f"Category '{category_name}' not found.")

def main():
    print("Welcome to Expense Tracker CLI")
    while True:
        print("\nMenu:")
        print("1. Enter Username")
        print("2. Add Category")
        print("3. Add Expense")
        print("4. List Expenses")
        print("5. Remove a User")
        print("6. Remove a Category")
        print("7. Remove an Expense")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            add_user(username)
        elif choice == "2":
            name = input("Enter category name: ")
            add_category(name)
        elif choice == "3":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            category_name = input("Enter category name: ")
            username = input("Enter username for this expense: ")
            add_expense(description, amount, category_name, username)
        elif choice == "4":
            list_expenses()
        elif choice == "5":
            username = input("Enter the username to remove: ")
            remove_user(username)
        elif choice == "6":
            category_name = input("Enter the category name to remove: ")
            remove_category(category_name)
        elif choice == "7":
            expense_id = int(input("Enter the ID of the expense to remove: "))
            remove_expense(expense_id)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
