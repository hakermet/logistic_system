# routes/urls.py
from django.urls import path
from . import views

app_name = 'routes'  # Важливо вказати app_name

urlpatterns = [
    path('', views.route_list, name='route_list'),
    path('create/', views.create_route, name='create_route'),
    path('<int:route_id>/', views.route_detail, name='route_detail'),
    path('<int:route_id>/update/', views.update_route, name='update_route'),
    path('<int:route_id>/delete/', views.delete_route, name='delete_route'),
    path('<int:route_id>/map/', views.map_view, name='map_view'),
    path('search/', views.search_routes, name='search_routes'),
    path('api/route/<int:route_id>/', views.get_route_data, name='get_route_data'),
]