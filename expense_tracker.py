import os

# This creates a file that stores your expenses
def initialize_file():
    if not os.path.exists('expenses.txt'):
        with open('expenses.txt', 'w') as file:
            file.write('Date,Amount,Category,Description\n')

# This adds new expenses to the file
def add_expense(date, amount, category, description):
    with open('expenses.txt', 'a') as file:
        file.write(f'{date},{amount},{category},{description}\n')
    print('✅ Expense added!')

# This shows all the expenses you’ve saved
def view_expenses():
    if not os.path.exists('expenses.txt'):
        print("No expenses found.")
        return
    with open('expenses.txt', 'r') as file:
        for line in file:
            print(line.strip())

# This adds up the total money you’ve spent
def total_expenses():
    total = 0
    if not os.path.exists('expenses.txt'):
        print("No expenses to total.")
        return
    with open('expenses.txt', 'r') as file:
        next(file)  # skip the header line
        for line in file:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                try:
                    total += float(parts[1])
                except ValueError:
                    pass
    print(f'Total expenses: ${total:.2f}')

# The main program that runs every time you start it
def main():
    initialize_file()
    while True:
        print("\nOptions: 1=Add Expense 2=View Expenses 3=Total Expenses 4=Quit")
        choice = input("Enter choice: ")
        if choice == '1':
            date = input("Date (YYYY-MM-DD): ")
            amount = input("Amount: ")
            category = input("Category: ")
            description = input("Description: ")
            add_expense(date, amount, category, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
