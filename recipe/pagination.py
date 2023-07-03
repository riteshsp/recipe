from rest_framework.pagination import PageNumberPagination

class PagePagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    