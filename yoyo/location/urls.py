from django.urls import path
from location.views import WeatherViewSet

urlpatterns = [
    path(
        "locations/<city>/",
        WeatherViewSet.as_view({"get": "list"}),
        name="location_weather",
    ),
]
