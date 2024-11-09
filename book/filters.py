# books/filters.py
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    minPrice = django_filters.NumberFilter(field_name="price", lookup_expr='gte', label="Minimum Price")
    maxPrice = django_filters.NumberFilter(field_name="price", lookup_expr='lte', label="Maximum Price")
    
    class Meta:
        model = Book
        fields = ['title',"description" ,'minPrice' ,'maxPrice']
