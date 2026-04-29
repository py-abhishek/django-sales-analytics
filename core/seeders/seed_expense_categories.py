from finance.models import ExpenseCategory
import json

def seed_expense_categories(business):
    

    with open('core/fixtures/expense_categories.json', 'r') as f:
        categories = json.load(f)
 
    expense_categories = []
    for item in categories:
        expense_categories.append(ExpenseCategory(
            name=item['name'],
            description=item['description'],
            business=business
        ))

    ExpenseCategory.objects.bulk_create(expense_categories)

        

        