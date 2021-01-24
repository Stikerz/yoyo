# Yoyo Python Engineering Test


This project was written using python3.x. & Angular 9. A pip requirements.txt
 file is included to install the dependencies
 
 ## Running with Docker
- A Docker Compose file is provided that will run the application in an
 isolated environment

- Make sure you have `docker & docker-compose` installed and that the Docker
 daemon is
 running
 
- Build & Run the image: `docker-compose up --build`

- Start using web app: `http://localhost:4200/`

NOTE: You will have to add your weather api key to `WEATHER_KEY`
 environment variable to run docker
 correctly  e.g `export
 WEATHER_KEY=*KEY*`
 
## Running with a virtual environment & NPM
  
#### Run Django Server

- To run the application in a virtual Python environment, follow these instructions. This example will create a virtual Python environment
- Run ```python3 -m venv env``` to create virtual environment called env
- Run ```source env/bin/activate``` to activate the virtual env
- Run ```pip install -r requirements.txt``` to install project requirements
- You can then run the migrations commands with `python manage.py
 makemigrations
` then
 `python manage.py
 makemigrations
` in the yoyo directory

- You can then run the server command with `python manage.py runserver`

- Start using api: `http://localhost:8000/api/locations/{city}/?days
={number_of_days}/`


NOTE: You will have to export your weather api key to `WEATHER_KEY`
 environment variable to run app
 correctly  e.g `export
 WEATHER_KEY="*KEY*"`

#### Run Angular App (Optional)

- Make sure you have Node installed on your machine (v13.11.0 used)

- Run `npm install -g @angular/cli` to install the angular command line tool

To check you have it installed correctly check the version `ng v`

- Install the dependencies by running `npm install` in the angular directory

- You can then run the app command with `ng serve`

- Start using web app: `http://localhost:4200/`


## Project Structure Notes

- The Backend Django Rest Framework  are stored in the `yoyo` folder
- The Front-End Angular app is in the `angular` folder, this is for testing
 purposes of the Django api application

- The tests are stored in the `yoyo/location/tests/` folder


## Testing
- Run `./manage.py test location.tests.test_location_views` 

NOTE: You will have to export your weather api key to `WEATHER_KEY`
 environment variable to run tests
 correctly  e.g `export
 WEATHER_KEY="*KEY*"`

## Coverage 

```

Module	                                  Statements Missing Exclude Coverage
-----------------------------------------------------------------------------
yoyo/location/__init__.py	               0	0	0	100%
yoyo/location/admin.py	                       1	0	0	100%
yoyo/location/migrations/__init__.py	       0	0	0	100%
yoyo/location/models.py                        1	0	0	100%
yoyo/location/serializers.py	               6	0	0	100%
yoyo/location/tests/support/assertions.py     11	0	0	100%
yoyo/location/tests/test_location_views.py    69	0	0	100%
yoyo/location/urls.py	                       3	0	0	100%
yoyo/location/utils/services.py	              42	0	0	100%
yoyo/location/views.py	                      18	0	0	100%
yoyo/yoyo/__init__.py	                       0	0	0	100%
yoyo/yoyo/settings.py	                      20	0	0	100%
yoyo/yoyo/urls.py	                       3	0	0	100%
-----------------------------------------------------------------------------
Total	                                     174	0	0	100%
```


## Assesment Spec


As an API user I want to get the minimum, maximum, average and median temperature for a given city and period of time.

####Requirements
- Create a Django application with RESTful API
- Django application must run locally
- API must be in the format /api/locations/{city}/?days={number_of_days}
- API must fetch weather data from some public API of your choice
- API must compute min, max, average, and median temperature
- Response format must be in the following structure:

```
{
    "maximum": value,
    "minimum": value,
    "average": value,
    "median": value,
}
```

#### Assumptions
- Max returns the highests temperature over the weather days averages
 collected 
- Min returns the lowest temperature over the weather days averages
 collected
- Average returns the average of the temperature averages over the
  specified amount of days of city weather
- Median returns the median of the temperature averages over the
  specified amount of days of city weather
  
