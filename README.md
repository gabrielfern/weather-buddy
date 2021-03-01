# Weather Buddy

This is a web application that shows weather reports for cities that you input. For the weather data, the [OpenWeather](https://openweathermap.org/) api is used. Results from the api are cached for a certain amount of time.

This webapp uses [Flask](https://flask.palletsprojects.com/) + [Svelte](https://svelte.dev/).

# Run in production

Run the following commands (you can use a python venv (`python -m venv .venv`) if you want to isolate the python environment)(don't forget to activate the venv).

* You need to set the environment variable `OPENWEATHER_API_KEY` to your OpenWeather api key

> pip install -r requirements.txt

> npm install

> npm run build

> gunicorn -w 1 app:app

# Run in development mode

You can start two development servers (one for back and other for frontend) as so (remember to install dependencies and to set the api key).

> FLASK_ENV=development flask run

> npm run dev

When running in production, a single server serves both back and frontend. Because you're running the api in a different port, you might need to configure the api url in the `rollup.config.js` file, setting a different value for `API_BASE_URL`.

# Docker

If you prefer you can also run the app using Docker.

> docker build -t weather-buddy .

> docker run -p 5000:5000 -e OPENWEATHER_API_KEY=$OPENWEATHER_API_KEY --name weather-buddy weather-buddy

# Heroku

You can easily deploy to Heroku, just remember to set `OPENWEATHER_API_KEY` and add buildpacks for python and node.

# Unit Tests

> python -m tests
