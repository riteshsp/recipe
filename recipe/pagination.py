from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PagePagination(PageNumberPagination):
    page_size = 15
    page_query_param = "page"

class PagePaginationAdmin(PageNumberPagination):
    page_size = 12
    page_query_param = "page"
    