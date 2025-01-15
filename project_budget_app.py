class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name.center(30, '*')}\n"
        items = ""
        for item in self.ledger:
            description = f"{item['description'][:23]:23}"
            amount = f"{item['amount']:7.2f}"
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    # Calculate total spending and percentage per category
    total_spent = 0
    category_spending = []
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        category_spending.append(spent)
        total_spent += spent

    percentages = [int((spent / total_spent) * 100 // 10 * 10) for spent in category_spending]

    # Create the chart header
    chart = "Percentage spent by category\n"

    # Create the percentage bars
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percentage in percentages:
            chart += " o " if percentage >= i else "   "
        chart += " \n"

    # Add the horizontal line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Add the category names vertically
    max_name_length = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_name_length) for category in categories]

    for i in range(max_name_length):
        chart += "     "
        for name in names:
            chart += f"{name[i]}  "
        chart += "\n"

    return chart.rstrip("\n")

# Example usage
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
clothing.deposit(500, 'initial deposit')
clothing.withdraw(50.00, 'new shoes')
clothing.withdraw(25.55, 'jacket')
clothing.withdraw(40.00, 'jeans')

auto = Category('Auto')
auto.deposit(1000, 'initial deposit')
auto.withdraw(15.00, 'gas')
auto.withdraw(10.00, 'car wash')
auto.withdraw(20.00, 'oil change')

print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))
