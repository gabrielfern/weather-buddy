from collections import OrderedDict


class CityCache:
    MAX_DICT_LEN = 10_000

    def __init__(self):
        self.cached_cities = OrderedDict()
        self.city_name_aliases = OrderedDict()

    def get_city(self, name):
        if name in self.cached_cities:
            return self._get_city(name)
        elif (name in self.city_name_aliases and
            self.city_name_aliases[name] in self.cached_cities):
            self.city_name_aliases.move_to_end(name)
            return self._get_city(self.city_name_aliases[name])

    def get_last_n(self, n):
        cities = []
        for k, _ in zip(reversed(self.cached_cities), range(n)):
            cities.append(self.cached_cities[k])
        return cities

    def set_city(self, name, city):
        self.cached_cities[city['name']] = city
        if name != city['name'] and name not in self.city_name_aliases:
            self.city_name_aliases[name] = city['name']
            self.cached_cities.move_to_end(city['name'])
        self._ensure_limit()

    def _get_city(self, name):
        self.cached_cities.move_to_end(name)
        return self.cached_cities[name]

    def _ensure_limit(self):
        if len(self.cached_cities) > self.MAX_DICT_LEN:
            self.cached_cities.popitem(last=False)

        if len(self.city_name_aliases) > self.MAX_DICT_LEN:
            self.city_name_aliases.popitem(last=False)
