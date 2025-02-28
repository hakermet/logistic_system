import requests

def get_route(pickup_address, delivery_address):
    """
    Отримує маршрут між двома адресами.
    """
    api_url = "https://router.project-osrm.org/route/v1/driving/"
    try:
        # Геокодування адрес до координат
        pickup_coords = geocode_address(pickup_address)
        delivery_coords = geocode_address(delivery_address)

        # Формуємо запит до OSRM
        route_url = f"{api_url}{pickup_coords[0]},{pickup_coords[1]};{delivery_coords[0]},{delivery_coords[1]}"
        response = requests.get(route_url, params={"overview": "full", "geometries": "geojson"})

        if response.status_code == 200:
            data = response.json()
            route_info = data['routes'][0]
            return {
                "distance": route_info["distance"] / 1000,  # Перетворення у км
                "duration": route_info["duration"] / 60,   # Перетворення у хвилини
                "route_points": route_info["geometry"]["coordinates"],
            }
        else:
            return None
    except Exception as e:
        print(f"Error fetching route: {e}")
        return None

def geocode_address(address):
    """
    Функція для перетворення адреси у координати.
    (Для цього можна використовувати, наприклад, Nominatim API)
    """
    api_url = "https://nominatim.openstreetmap.org/search"
    response = requests.get(api_url, params={"q": address, "format": "json", "limit": 1})

    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return float(data["lon"]), float(data["lat"])
    return None
