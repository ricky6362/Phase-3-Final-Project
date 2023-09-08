# Expense Tracker CLI

## Overview

The Expense Tracker CLI is a command-line interface (CLI) application that allows users to manage their expenses. This application enables users to record their expenses, categorize them, and list or remove expenses as needed.

## Features

- **User Management**: Users can create their profiles by entering a unique username.
- **Category Management**: Users can add expense categories to better organize their expenses.
- **Expense Recording**: Users can add expenses with descriptions, amounts, and associated categories.
- **Expense Listing**: Users can view a list of recorded expenses, including their descriptions, amounts, categories, and associated users.
- **User Removal**: Users can be removed from the system.
- **Category Removal**: Categories can be removed from the system.
- **Expense Removal**: Users can delete specific expenses by providing their unique IDs.
- **Data Persistence**: Data is stored in an SQLite database, ensuring that recorded expenses are saved between sessions.

## Getting Started

### Prerequisites

- Python 3.x
- Pipenv (for managing dependencies)

### Installation

1. Clone the repository to your local machine:

   ```
   git clone git@github.com:ricky6362/Phase-3-Final-Project.git

2. Navigate to the project directory:
    ```
    cd Phase-3-Final-Project

3. Install the project dependencies using Pipenv:
    ```
    pipenv install

## Usage
To run the Expense Tracker CLI, use the following command:
    
    python expense_tracker.py

Follow the on-screen instructions to interact with the application. You can perform actions like adding categories, adding expenses, listing expenses, and removing expenses.

## Database
The application uses an SQLite database named database.db to store user profiles, categories, and expense records. You can back up or migrate this database as needed.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
This project was inspired by the need for a simple and effective expense tracking tool.
Special thanks to SQLAlchemy for providing the database functionality.

## Author
**Richard Kimani** 