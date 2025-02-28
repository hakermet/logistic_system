from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Route
from .forms import RouteForm
from django.db import models
GOOGLE_MAPS_API_KEY = 'AIzaSyABC7deHCmQO5p-62DciZhICHzSCwjUxDM'  # Замініть на ваш ключ
MAPBOX_TOKEN = 'pk.eyJ1IjoibWV0Z2hvc3QiLCJhIjoiY203bHpiYnoyMGY0bTJrczZseXM1MHFzaSJ9.rWDXo6GsQmBgMBsmMhagiw'  # Замініть на ваш токен

@login_required
def route_list(request):
    routes = Route.objects.all().order_by('-created_at')
    return render(request, 'routes/route_list.html', {'routes': routes})

@login_required
def create_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            route = form.save(commit=False)
            route.user = request.user  # Збереження поточного користувача
            route.save()
            return redirect('routes:route_list')
    else:
        form = RouteForm()
    
    return render(request, 'routes/create_route.html', {
        'form': form,
        'google_maps_api_key': GOOGLE_MAPS_API_KEY,
        'mapbox_token': MAPBOX_TOKEN
    })

@login_required
def route_detail(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    return render(request, 'routes/route_detail.html', {
        'route': route,
        'google_maps_api_key': GOOGLE_MAPS_API_KEY
    })

@login_required
def map_view(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    return render(request, 'routes/map.html', {
        'route': route,
        'google_maps_api_key': GOOGLE_MAPS_API_KEY
    })

@login_required
def delete_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    route.delete()
    return redirect('routes:route_list')

@login_required
def update_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('routes:route_detail', route_id=route.id)
    else:
        form = RouteForm(instance=route)
    
    return render(request, 'routes/update_route.html', {
        'form': form,
        'route': route,
        'google_maps_api_key': GOOGLE_MAPS_API_KEY,
        'mapbox_token': MAPBOX_TOKEN
    })

@login_required
def get_route_data(request, route_id):
    try:
        route = get_object_or_404(Route, id=route_id)
        data = {
            'start_place': route.start_place,
            'end_place': route.end_place,
            'start_lat': float(route.start_lat),
            'start_lng': float(route.start_lng),
            'end_lat': float(route.end_lat),
            'end_lng': float(route.end_lng),
            'distance': float(route.distance),
            'duration': route.duration
        }
        return JsonResponse(data)
    except Route.DoesNotExist:
        return JsonResponse({'error': 'Маршрут не знайдено'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def search_routes(request):
    """Пошук маршрутів за початковою або кінцевою точкою"""
    query = request.GET.get('query', '')
    
    if query:
        # Пошук по обох полях (початкова та кінцева точка)
        routes = Route.objects.filter(
            models.Q(start_place__icontains=query) |
            models.Q(end_place__icontains=query)
        ).order_by('-created_at')
        
        print(f"Search query: {query}")  # Для відлагодження
        print(f"Found routes: {routes.count()}")  # Для відлагодження
    else:
        routes = Route.objects.none()
    
    context = {
        'routes': routes,
        'query': query,
        'google_maps_api_key': GOOGLE_MAPS_API_KEY
    }
    
    return render(request, 'routes/search_routes.html', context)