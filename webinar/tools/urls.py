from django.urls import path
from .views import index
from .views import prepare_excel_index
from .views import prepare_db_excel

urlpatterns = [
    path('', index, name='tools'),
    path('prepare-excel', prepare_excel_index, name='prepare_excel_index'),
    path('excel_db_prepare', prepare_db_excel, name='prepare_db_excel')
]
