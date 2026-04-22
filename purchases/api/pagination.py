from rest_framework.pagination import PageNumberPagination

class SupplierPagination(PageNumberPagination):
    page_size = 100 # default results per page
    page_size_query_param = 'page_size' # to override result
    max_page_size = 200 # safty limit