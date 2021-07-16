from django.urls import path
from .views import index
from .views import prepare_excel

urlpatterns = [
    path('', index, name='tools'),
    path('prepare-excel', prepare_excel, name='prepare_excel')
]