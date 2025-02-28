from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title', 'description', 'cargo_type', 'weight', 'status']  # Включаємо всі необхідні поля

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Введіть назву замовлення'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Введіть опис замовлення'})
        self.fields['weight'].widget.attrs.update({'placeholder': 'Введіть вагу (кг)'})