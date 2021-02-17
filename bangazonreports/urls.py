from django.urls import path
from .views import inexpensiveproduct_list

urlpatterns = [
    path('reports/inexpensiveproducts', inexpensiveproduct_list),
]