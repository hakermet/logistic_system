# logistics_system/logistics_system/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('routes/', include('routes.urls', namespace='routes')),
    path('', RedirectView.as_view(pattern_name='routes:route_list'), name='home'),
    path('orders/', include('orders.urls')),
    path('accounts/', include('users.urls')),
]