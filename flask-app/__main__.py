from urllib.error import HTTPError
from flask import Flask, jsonify, request
from .openweather_proxy import OpenWeatherProxy
from .constants import N_ELEMS_RETURNED, NOT_FOUND, INTERNAL_ERROR

app = Flask(__name__, static_folder='../svelte-app/public', static_url_path='')
openweather_proxy = OpenWeatherProxy()


@app.route('/api/weather', methods=['GET'])
def get_weather():
    n_elems = N_ELEMS_RETURNED
    if 'max' in request.args:
        n_elems = int(request.args['max'])

    return jsonify(openweather_proxy.last_n(n_elems))


@app.route('/api/weather/<name>', methods=['GET'])
def get_city_weather(name):
    try:
        return openweather_proxy.retrieve_city(name)

    except HTTPError as e:
        if e.code == 404:
            return NOT_FOUND
        else:
            return INTERNAL_ERROR


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.after_request
def cors(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run()
