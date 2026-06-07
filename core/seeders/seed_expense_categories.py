from finance.models import ExpenseCategory
import json

def seed_expense_categories(data, business):
    

    with open(data, 'r') as f:
        categories = json.load(f)
 
    expense_categories = []
    for item in categories:
        expense_categories.append(ExpenseCategory(
            name=item['name'],
            description=item['description'],
            business=business
        ))

    ExpenseCategory.objects.bulk_create(expense_categories)

        

        