from django.urls import path
from .views import inexpensiveproduct_list, expensiveproduct_list

urlpatterns = [
    path('reports/inexpensiveproducts', inexpensiveproduct_list),
    path('reports/expensiveproducts', expensiveproduct_list),
]