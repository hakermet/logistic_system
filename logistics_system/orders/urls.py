from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.create_order, name='create_order'),
    path('update/<int:order_id>/', views.update_order, name='update_order'),
    path('delete/<int:order_id>/', views.delete_order, name='delete_order'),
    path('search/', views.search_orders, name='search_orders'),
]