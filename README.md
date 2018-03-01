![alt Flask-Admin ](https://habrastorage.org/webt/fb/w2/42/fbw242ettd1fay8l4rwt3xtd-ac.png)
![alt Flask-security ](https://habrastorage.org/webt/hq/ep/wj/hqepwjev4pucazix5ztzqw9pvk0.png)

# Flask-Securyty & Flask-Admin & MongoDB in one app

This code base serves as starting point for writing your next Flask application.

## Code characteristics

* Well organized directories with lots of comments
    * app
        * models
        * static
        * templates
        * views
* Sends error emails to admins for unhandled exceptions


## Setting up a development environment

We assume that you have `git`, `virtualenv` and `mongoDB` installed.

    cd ~
    virtualenv env
    . env/bin/activate
    mkdir -p ~/www/my_app
    cd www
    git clone https://github.com/Alexmod/flask-security-flask-admin-mongodb.git  my_app
    cd my_app/
    pip install -r requirements.txt

   
# Configuring SMTP

Edit the `local_settings.py` file.

Specifically set all the MAIL_... settings to match your SMTP settings

Note that Google's SMTP server requires the configuration of "less secure apps".
See https://support.google.com/accounts/answer/6010255?hl=en

Note that Yahoo's SMTP server requires the configuration of "Allow apps that use less secure sign in".
See https://help.yahoo.com/kb/SLN27791.html



## Running the app

    # Start the Flask development web server
    python manage.py runserver


Point your web browser to http://localhost:5000/

You can make use of the following users:
- email `user@example.com` with password `Password1`.
- email `admin@example.com` with password `Password1`.
