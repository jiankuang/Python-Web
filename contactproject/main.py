"""`main` is the top level module for your Flask application."""

import os
import MySQLdb

# Import the Flask Framework
from flask import Flask, render_template

# These environment variables are configured in app.yaml.
CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')

def connect_to_cloudsql():
    # When deployed to App Engine, the `SERVER_SOFTWARE` environment variable
    # will be set to 'Google App Engine/version'.
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        # Connect using the unix socket located at
        # /cloudsql/cloudsql-connection-name.
        cloudsql_unix_socket = os.path.join(
            '/cloudsql', CLOUDSQL_CONNECTION_NAME)

        db = MySQLdb.connect(
            unix_socket=cloudsql_unix_socket,
            user=CLOUDSQL_USER,
            passwd=CLOUDSQL_PASSWORD)

    # If the unix socket is unavailable, then try to connect using TCP. This
    # will work if you're running a local MySQL server or using the Cloud SQL
    # proxy, for example:
    #
    #   $ cloud_sql_proxy -instances=your-connection-name=tcp:3306
    #
    else:
        db = MySQLdb.connect(
            host='127.0.0.1', user=CLOUDSQL_USER, passwd=CLOUDSQL_PASSWORD)

    return db

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def index():
    contacts = []
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute('USE slw_film')
    cursor.execute('SELECT * FROM slw_directory')
    for r in cursor.fetchall():
        contacts.append(r)
    """Return a friendly HTTP greeting."""
    return render_template('index.html', contacts=contacts)

@app.route('/contact/<int:id>')
def show_contact(id):
    # show the contact with the given id, the id is an integer
    contacts = []
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute('USE slw_film')
    cursor.execute('SELECT * FROM slw_directory')
    for r in cursor.fetchall():
        contacts.append(r)

    return render_template('contact.html', contact=contacts[id-1])

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
