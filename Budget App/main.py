class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description.capitalize()})

    def withdraw(self, amount, description=''):
        if self.check_founds(amount):
            self.ledger.append({'amount': -amount, 'description': description.capitalize()})
            return True
        return False
        

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_founds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
        
    def check_founds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        title = f"\n{self.name.title():*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
        total = f"Total: {self.get_balance():.2f}\n"
        return title + items + total


def create_spend_chart(categories):
    # Calculate the percentage spent in each category
    total_withdrawals = 0
    percentages = []
    for category in categories:
        withdrawals = 0
        for item in category.ledger:
            if item['amount'] < 0:
                withdrawals += abs(item['amount'])
        total_withdrawals += withdrawals
        percentages.append(withdrawals)

    for i in range(len(percentages)):
        percentages[i] = percentages[i] / total_withdrawals * 100
        percentages[i] = percentages[i] // 10 * 10

    # Create the chart
    chart = 'Percentage spent by category\n'
    for i in range(100, -10, -10):
        chart += f'{i:3d}| '
        for percentage in percentages:
            if percentage >= i:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'

    chart += '    ' + '-' * (3 * len(categories) + 1) + '\n'

    # Find the longest category name
    max_length = 0
    for category in categories:
        if len(category.name) > max_length:
            max_length = len(category.name)

    # Add the category names to the chart
    for i in range(max_length):
        chart += '     '
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + ' '
            else:
                chart += '  '
        chart += '\n'

    return chart.rstrip()

# Create
food_category = Category('food')
clothing_category = Category('clothing category')
entertainment_category = Category('movie')

food_category.deposit(1000, 'initial deposit')
food_category.withdraw(10.15, 'groceries')
food_category.withdraw(15.89, 'restaurant and more food')
food_category.transfer(50.00, clothing_category)
food_category.withdraw(125.00, 'entertainment')

print(food_category)

categories = [food_category, clothing_category, entertainment_category]

# Call the create_spend_chart function with the categories list
chart = create_spend_chart(categories)

# Print the resulting chart
print(chart)


