from django.contrib import admin
from .models import Route

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('start_place', 'end_place', 'distance', 'duration', 'created_at')
    search_fields = ('start_place', 'end_place')
    list_filter = ('created_at',)