from location.serializers import WeatherSerializer
from location.utils.services import get_city_weather_info
from rest_framework import status, viewsets
from rest_framework.response import Response


class WeatherViewSet(viewsets.ViewSet):
    serializer_class = WeatherSerializer

    def validate_input(self, days):
        if not days.isnumeric():
            raise Exception(
                f"Days value {days} " f"is not a correct datatype must be number "
            )

        if int(days) > 7 or int(days) < 1:
            raise Exception(f"Days value {days} " f"is not in correct range 1-7 ")

    def list(self, request, **kwargs):
        city = kwargs.get("city")
        days = self.request.query_params.get("days", "1")
        self.validate_input(days)
        data = get_city_weather_info(city, days)
        serializer = WeatherSerializer(instance=data)
        return Response(serializer.data, status=status.HTTP_200_OK)
