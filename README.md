# Web report of Monaco 2018 Racing

It is an educational project on FoxMinded platform.
The task was creating a  flask application to REST API using Flask API package 
and adding swagger using flasgger.

## Improvements

First wasn't removed HTML part of the application.
API was implemented and made to work together with HTML templates.
In general was improved User-Friendliness of the app.
- created function for the automatic search of data-files. It allowed remove DATA_PATH variable from the ```.env``` or ```app.settings```.
- instead of several functions, one class was created, which contains all the logic of working with the source data. In addition, it provides storage of information without the need to generate it for each request.
  - class initialization logic is borrowed from packages such as flask_restful and flask_bootstrap. To do this, the ```init_app``` function was created, which is called when creating an instance of the application and fills the class with data.
- added some buttons to the navbar including "Site map" and "API".
- "API" menu contains different variants of imagine API data.
- as an experiment html page with base navbar and Swagger interface was created within, which allowed after use Swagger return to the main page (but it forced to abandon the use of the package Flasgger).

## Getting Started
 
This application is created with pipenv usage.
Also file ```.env``` was added.
This file contains variables ```FLASK_APP``` and ```FLASK_ENV```. 
In normal conditions they do not need to be changed.
More information of Shell Variables you can find 
[here](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/).

So for the starters you need to launch pipenv:

```
pipenv install
pipenv shell
```  

For the checking Shell Variables use:

```
printenv FLASK_APP
```

## Usage

```
flask run
```

Open the HTML link in the terminal to get the access to the program.
On the HTML page you can use following addresses:


- [http://localhost:5000/report](http://localhost:5000/report)
- [http://localhost:5000/report/drivers/](http://localhost:5000/report/drivers/)
- [http://localhost:5000/report/drivers/?driver_id=SVF](http://localhost:5000/report/drivers/?driver_id=SVF)
- [http://localhost:5000/report/drivers/?order=desc](http://localhost:5000/report/drivers/?order=desc)

- [http://localhost:5000/api/v1/report/](http://localhost:5000/api/v1/report/)
- [http://localhost:5000/api/docs/include](http://localhost:5000/api/docs/include)

All routes available:

- [http://localhost:5000/site-map](http://localhost:5000/site-map)


## Running the tests

To run the tests you need to install ```develop``` packages:
```bash
pipenv install --dev
```

After that to run the tests you must write:

```bash 
pytest
coverage run -m pytest
```
 