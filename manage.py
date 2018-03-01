"""This file sets up a command line manager.

Use "python manage.py" for a list of available commands.
Use "python manage.py runserver" to start the develop web  on localhost:5000.
Use "python manage.py runserver --help" for additional runserver options.
"""

from flask_script import Manager
from app import create_app

# Setup Flask-Script with command line commands
manager = Manager(create_app)

if __name__ == "__main__":
    # python manage.py                      # shows available commands
    # python manage.py runserver --help     # shows available runserver options
    manager.run()
