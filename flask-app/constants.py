from os import environ

N_ELEMS_RETURNED = 5

OPENWEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'

OPENWEATHER_API_KEY = environ['OPENWEATHER_API_KEY']

NOT_FOUND = ({
    'message': 'City was not found'
}, 404)

INTERNAL_ERROR = ({
    'message': 'An error has occurred'
}, 500)
