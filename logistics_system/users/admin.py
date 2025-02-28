# logistics_system/users/admin.py
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')  # Поля, які ви хочете відображати в списку
    list_filter = ('role', 'is_staff', 'is_active')  # Фільтри для списку
    search_fields = ('username', 'email')  # Поля для пошуку

admin.site.register(CustomUser, CustomUserAdmin)