from django.shortcuts import render
from django.views.generic import View
from django.db.models import F
from datetime import date, timedelta, datetime
import json
from django.http import JsonResponse

from inventory.models import Product, ProductCategory
from sales.models import SaleItem
from ..services import product_analysis 


class ProductReportView(View):
    def get(self, request):
        product_categories = ProductCategory.objects.all().order_by('name')

        # calling function from services layer
        insights = product_analysis.get_insights()

        context = {
            'product_categories': product_categories
        }

        context.update(insights)

        return render(request, 'reports/product_report.html', context)
    

# Filter API
def get_filtered_data(request):
    print('API')
    if request.method == 'POST':
        filter_values = json.loads(request.body)

        # getting str date and converting to date value
        raw_f_date = filter_values.get('fromDate')
        raw_t_date = filter_values.get('toDate')
        from_date = None
        to_date = None

        if raw_f_date:
            from_date = datetime.strptime((raw_f_date), '%Y-%m-%d').date()

        if raw_t_date:
            to_date = datetime.strptime((raw_t_date), '%Y-%m-%d').date()

        category_id = filter_values.get('category')
        category = 'All Categories'
        if category_id:
            category_id = int(category_id)
            category = ProductCategory.objects.get(id=category_id).name
        

        print(category)

        insights = product_analysis.get_insights(from_date, to_date, category_id)

        insights['results_for'] = {
            'date':{
                'from': from_date or 'Starting',
                'to': to_date or 'Now'
            },
            'category': category
        }


        return JsonResponse(insights,  safe=False)