from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('Providers/',views.ProviderList.as_view()),
    path('Providers/<int:pk>',views.ProviderDetail.as_view()),
    path('Products/',views.ProductList.as_view()),
    path('Producst/<int:pk>',views.ProductDetail.as_view()),
    path('Users/', views.UserList.as_view()),
    path('Users/<int:pk>', views.UserDetail.as_view()),
    path('Employees/', views.EmployeList.as_view()),
    path('Employees/<int:pk>', views.EmployesDetail.as_view()),
    path('Historicals/', views.HistoricalList.as_view()),
    path('Historicals/<int:pk>', views.HistoricalDetail.as_view()),
    path('Customers/', views.CustomerList.as_view()),
    path('Customers/<int:pk>', views.CustomerDetail.as_view()),
    path('Sales/', views.SaleList.as_view()),
    path('Sales/<int:pk>', views.SaleDetail.as_view()),
    path('Product_has_sale/', views.Product_has_SaleList.as_view()),
    path('Product_has_sale/<int:pk>', views.Product_has_SaleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)