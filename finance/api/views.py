
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django.db.models import Q

from finance.models import Expense, ExpenseCategory
from .serializers import ExpenseSerializer, ExpenseCategorySerializer


def get_business_id(request):
    return request.session.get('business_id')

# Search expenses
class ExpensesSearchView(ListAPIView):
    serializer_class = ExpenseSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'category__name']

    def get_queryset(self):
        queryset = Expense.objects.filter(
            business_id=get_business_id(self.request)
        ).order_by('-expense_date')
        
        return queryset


# Search exp categories
class ExpCategoriesSearchView(ListAPIView):
    serializer_class = ExpenseCategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return ExpenseCategory.objects.filter(
            business_id=get_business_id(self.request)
        ).order_by('-created_at')
    