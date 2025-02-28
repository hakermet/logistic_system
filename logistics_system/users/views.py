# logistics_system/users/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Увійти автоматично після реєстрації
            return redirect('route_list')  # Перенаправлення на список маршрутів або іншу сторінку
    else:
        form = RegistrationForm()
    return render(request, 'registration/registr.html', {'form': form})