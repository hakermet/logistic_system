from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cargo_type', 'weight', 'pickup_address', 'delivery_address', 'created_at')
    list_filter = ('cargo_type', 'created_at')
    search_fields = ('pickup_address', 'delivery_address', 'user__username')


