# spam-pkg
The official repository for the [`spam` package manager](https://github.com/jwinnie/spam). It is hosted on Heroku at https://spam-pkg.herokuapp.com. Individual packages are in the [/packages](/packages) directory. To install them:
```
$ spam get spam-pkg.herokuapp.com/<tarball_name>
```

## Developing
The web app is a simple Python3/Flask server. Before developing, you must enter the Python `virtualenv`. This configures the environment:
```
$ source venv/bin/activate
```
To run the app, it is recommended to use `gunicorn`:
```
$ gunicorn --pythonpath web main:app
```
However, it *is* a Flask app, so this is okay:
```
$ export FLASK_APP=web/main.py
$ flask run
```
If any new dependencies are added via `pip`, they must be stated:
```
$ pip freeze > web/requirements.txt
```
To push your changes Heroku (you need to have Heroku CLI and edit access to the Heroku project):
```
$ git push heroku master
```

