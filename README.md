# Web report of Monaco 2018 Racing

It is an educational project on FoxMinded platform.
The task was creating a  flask application to REST API using Flask API package 
and adding swagger using flasgger.

## Getting Started

The first running of the application consists from 3 steps:
 
- [preparing](#preparing) the virtual environment and install dependencies;
- [initialization](#initialization) of the database;
- [running](#running) the flask application.

### Preparing

This application is created with pipenv usage.
Also file `.env` was added.
This file contains variables `FLASK_APP` and `FLASK_ENV`. 
In normal conditions they do not need to be changed.
More information of Shell Variables you can find 
[here](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/).

So for the starters you need to launch pipenv:

`pipenv install`

Next, activate the Pipenv shell:

`pipenv shell`  

For the checking Shell Variables use:

`printenv FLASK_APP`

Project also contains the `requirements.txt` file witch help to install dependencies with `pip` usage. 
So alternatively you can use `pip install -r requirements.txt`.

### Initialization

Before first start of application data about racers are kept in files `abbreviations.txt, aend.log, start.log`.
To copy them into the database you need to once run command `flask init-db`.
This command must be run in the virtual environment after installation all the requirements.
After that in the project folder will create `app.db` file with all data.
Project not contains the migration mechanism so command launch `flask init-db` again will remove an old database and will create new.

### Running

`flask run`

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

To run the tests you need to install `develop` packages:

`pipenv install --dev`

After that to run the tests you must write:

`pytest`

`coverage run -m pytest`

`covarage report`
 