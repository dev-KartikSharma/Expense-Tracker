#Expense Tracker

# category - Food/ entertainment/ travel/ EMI/ clothes/ rent/ misc

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
    
    def __str__(self):
        return f"{self.category} ₹{self.amount} - {self.description}"

class Tracker:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self, amount, category, description):
        self.expenses.append(Expense(amount,category,description))
        return "---- Expense added successfully! ----\n"
    
    def view_expenses(self):
        i = 1
        print("\n==== List of all Expenses ====\n")
        for _ in self.expenses:
            print(f"{i}.) {_}")
            i += 1
        print()

    def total_spent(self):
        return sum(expense.amount for expense in self.expenses)

    def clear_expenses(self):
        print("\n==== Clearing Expenses ====\n")
        self.expenses.clear()
        return f"---- All Expenses are cleared. ----"

    def filter_category(self, category):
        category = category.lower()
        print(f"\n==== Showing for {category.capitalize()} ====")
        for expcategory in self.expenses:
            if expcategory == category:
                print(expcategory)
            
        
def main():
    exp_tracker = Tracker()
    print("===== Expense Tracker =====")
    valid_categories = ["Food", "Entertainment", "Travel", "EMI", "Clothes", "Rent", "Misc"]
    while True:
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Total Spent")
        print("4. Filter by Category")
        print("5. Clear Expenses")
        print("6. Exit\n")
        ch = int(input("Enter choice (1-6): "))
        if ch == 1:
            amount = int(input("Amount (₹): "))
            print("Available categories: Food / Entertainment / Travel / EMI / Clothes / Rent / Misc")
            category = input("Category: ").strip().capitalize()
            if category not in valid_categories:
                print("Invalid Choice!! ")
                continue
            description = input("Desc: ")
            print(exp_tracker.add_expense(amount, category, description))
        elif ch == 2:
            print("\n==== Total Money Spent ====\n")
            print(f"Total spent so far(₹): {exp_tracker.total_spent()}\n")
        elif ch == 3:
            exp_tracker.total_spent()
        elif ch == 4:
            print("Available categories: Food / Entertainment / Travel / EMI / Clothes / Rent / Misc")
            category = input("Category: ").strip().capitalize()
            if category not in valid_categories:
                print("Invalid Choice!! ")
                continue
            else:
                print(exp_tracker.filter_category(category))
        elif ch == 5:
            print(exp_tracker.clear_expenses())
        elif ch == 6:
            print("See you again!!")
            break
    
if __name__ == "__main__":
    main()