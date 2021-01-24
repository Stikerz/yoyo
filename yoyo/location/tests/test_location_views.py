from unittest import mock

from django.test import TestCase
from location.tests.support.assertions import assert_valid_schema
from requests.exceptions import (ConnectionError, HTTPError, RequestException,
                                 Timeout)
from rest_framework import status


class LocationViewTest(TestCase):
    def test_get_weather(self):
        city_name = "Paris"
        response = self.client.get(f"/api/locations/{city_name}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 4)
        assert_valid_schema(response.json(), "location_schema.json")

    def test_get_weather_days(self):
        city_name = "Paris"
        response = self.client.get(f"/api/locations/{city_name}/?days=5")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 4)
        assert_valid_schema(response.json(), "location_schema.json")

    def test_missing_weather_missing_days_not_numeric(self):
        with self.assertRaises(Exception) as cm:
            city_name = "Paris"
            days = "gooo"
            self.client.get(f"/api/locations/{city_name}/?days={days}")
        self.assertEqual(
            str(cm.exception),
            f"Days value {days} " f"is not a correct datatype must be number ",
        )

    def test_missing_weather_missing_days_more_than_max(self):
        with self.assertRaises(Exception) as cm:
            city_name = "Paris"
            days = 50
            self.client.get(f"/api/locations/{city_name}/?days={days}")
        self.assertEqual(
            str(cm.exception), f"Days value {days} " f"is not in correct range 1-7 "
        )

    def test_get_weather_false_city(self):
        with self.assertRaises(Exception) as cm:
            city_name = "Fooboo"
            self.client.get(f"/api/locations/{city_name}/")
        self.assertEqual(
            str(cm.exception),
            f"Error retrieving weather:{city_name} City",
        )

    @mock.patch("location.utils.services.WEATHER_KEY", None)
    def test_missing_weather_env(self):
        with self.assertRaises(Exception) as cm:
            city_name = "Paris"
            self.client.get(f"/api/locations/{city_name}/")
        self.assertEqual(
            str(cm.exception),
            f"Error retrieving weather key from env variable 'WEATHER_KEY'  "
            f"please make sure key is set",
        )

    @mock.patch("location.utils.services.requests.get", side_effect=ConnectionError)
    def test_get_weather_connection_err(self, mock_request):
        with self.assertRaises(Exception) as cm:
            city_name = "Paris"
            self.client.get(f"/api/locations/{city_name}/")
        self.assertEqual(str(cm.exception), f"Connection Error: ")

    @mock.patch("location.utils.services.requests.get", side_effect=Timeout)
    def test_get_weather_timeout(self, mock_request):
        with self.assertRaises(Exception) as cm:
            city_name = "Paris"
            self.client.get(f"/api/locations/{city_name}/")
        self.assertEqual(str(cm.exception), f"Timeout Error: ")

    @mock.patch("location.utils.services.requests.get", side_effect=HTTPError)
    def test_get_weather_http_err(self, mock_request):
        with self.assertRaises(Exception) as cm:
            city_name = "Paris"
            self.client.get(f"/api/locations/{city_name}/")
        self.assertEqual(str(cm.exception), f"Http Error: ")

    @mock.patch("location.utils.services.requests.get", side_effect=RequestException)
    def test_get_weather_req_err(self, mock_request):
        with self.assertRaises(Exception) as cm:
            city_name = "Paris"
            self.client.get(f"/api/locations/{city_name}/")
        self.assertEqual(str(cm.exception), f"Error: ")
