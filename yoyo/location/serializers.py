from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    maximum = serializers.FloatField(read_only=True)
    minimum = serializers.FloatField(read_only=True)
    average = serializers.FloatField(read_only=True)
    median = serializers.FloatField(read_only=True)
