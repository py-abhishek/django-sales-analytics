from finance.models import Expense, ExpenseCategory
import json


def seed_expenses(data, business, user):

    with open(data, 'r') as f:
        expense_list = json.load(f)

    expenses = []

    for item in expense_list:
        expenses.append(Expense(
            name=item['name'],
            category=ExpenseCategory.objects.get(name=item['category'], business=business),
            amount=item['amount'],
            description= item['description'],
            expense_date=item['expense_date'],
            business=business,
            created_by=user
        ))

    Expense.objects.bulk_create(expenses)

        