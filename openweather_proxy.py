import urllib
import json
from city_cache import CityCache
from time import time
from constants import OPENWEATHER_API_URL, OPENWEATHER_API_KEY


class OpenWeatherProxy:
    CACHE_TTL = 60 * 5

    def __init__(self):
        self.city_cache = CityCache()

    def retrieve_city(self, name):
        city = self.city_cache.get_city(name)
        if not city or not self._is_cached_city_valid(city):
            city = self._retrieve_city(name)
        return city

    def last_n(self, n):
        cities = []
        for city in self.city_cache.get_last_n(n):
            if not self._is_cached_city_valid(city):
                city = self._retrieve_city(city['name'])
            cities.append(city)
        return cities

    def _retrieve_city(self, name):
        city = self._make_city(self._call_openweather(name))
        self.city_cache.set_city(name, city)
        return city

    def _is_cached_city_valid(self, city):
        return city['timestamp'] >= (time() - self.CACHE_TTL)

    def _call_openweather(self, name):
        query = '?'
        query += urllib.parse.urlencode({
            'q': name, 'appid': OPENWEATHER_API_KEY, 'units': 'metric'
        })
        r = urllib.request.urlopen(OPENWEATHER_API_URL + query)
        return json.loads(r.read())

    def _make_city(self, api_res):
        return {
            'name': api_res['name'],
            'temperature': api_res['main']['temp'],
            'weather': api_res['weather'][0]['description'],
            'timestamp': time()
        }
