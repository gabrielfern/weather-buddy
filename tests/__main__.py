import unittest
import sys

sys.path.append('app')
from city_cache import CityCache


class TestCityCache(unittest.TestCase):
    def test_get_last_added(self):
        city_cache = CityCache()
        city = {'name': 'last'}

        city_cache.set_city('last', city)
        self.assertEqual(city_cache.get_city('last'), city)


    def test_cached_cities_max_len(self):
        city_cache = CityCache()

        for i in range(city_cache.MAX_DICT_LEN * 2):
            city = {'name': str(i)}
            city_cache.set_city(city['name'], city)

        self.assertEqual(
            len(city_cache.cached_cities), city_cache.MAX_DICT_LEN
        )
        self.assertEqual(len(city_cache.city_name_aliases), 0)


    def test_aliases_max_len(self):
        city_cache = CityCache()
        city = {'name': 'test'}

        for i in range(city_cache.MAX_DICT_LEN * 2):
            city_cache.set_city(str(i), city)

        self.assertEqual(len(city_cache.cached_cities), 1)
        self.assertEqual(len(
            city_cache.city_name_aliases), city_cache.MAX_DICT_LEN
        )


    def test_get_last_n(self):
        city_cache = CityCache()
        cities = [{'name': str(i)} for i in range(5)]

        for city in cities:
            city_cache.set_city(city['name'], city)

        self.assertEqual(
            city_cache.get_last_n(5), list(reversed(cities))
        )


    def test_get_last_n_order_changed(self):
        city_cache = CityCache()
        cities = [{'name': '1'}, {'name': '2'}, {'name': '3'}]

        for city in cities:
            city_cache.set_city(city['name'], city)

        city_cache.get_city('1')
        city_cache.get_city('2')

        self.assertEqual(
            city_cache.get_last_n(5),
            [{'name': '2'}, {'name': '1'}, {'name': '3'}]
        )


    def test_single_city_multiple_aliases(self):
        city_cache = CityCache()
        city = {'name': 'test'}

        city_cache.set_city('test', city)
        city_cache.set_city('TEST', city)
        city_cache.set_city('Test', city)

        self.assertEqual(list(city_cache.cached_cities.keys()), ['test'])
        self.assertEqual(
            list(city_cache.city_name_aliases.keys()), ['TEST', 'Test']
        )

        self.assertEqual(city_cache.get_city('Test'), city)
        self.assertEqual(city_cache.get_city('TEST'), city)
        self.assertEqual(city_cache.get_city('test'), city)

        self.assertEqual(len(city_cache.cached_cities), 1)
        self.assertEqual(len(city_cache.city_name_aliases), 2)


    def test_city_not_exists(self):
        city_cache = CityCache()
        self.assertFalse(city_cache.get_city('nan'))


if __name__ == '__main__':
    unittest.main()
