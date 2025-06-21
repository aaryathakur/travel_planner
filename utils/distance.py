from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_distance(source, destination):
    try:
        geolocator = Nominatim(user_agent="trip_planner_app")

        # Get coordinates for source
        loc1 = geolocator.geocode(source)
        if not loc1:
            print(f"Could not locate source: {source}")
            return None

        # Get coordinates for destination
        loc2 = geolocator.geocode(destination)
        if not loc2:
            print(f"Could not locate destination: {destination}")
            return None

        # Calculate distance
        coords_1 = (loc1.latitude, loc1.longitude)
        coords_2 = (loc2.latitude, loc2.longitude)

        distance_km = geodesic(coords_1, coords_2).km
        return round(distance_km, 2)

    except Exception as e:
        print(f"Error in get_distance: {e}")
        return None
