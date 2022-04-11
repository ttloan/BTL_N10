import pyodbc
from flask import current_app


def connect_db(app):
    config = {
        'SERVER': app.config['DB_HOST'],
        'DATABASE': app.config['DB_NAME'],
        'UID': app.config['DB_USER'],
        'PWD': app.config['DB_PASS'],
        'DRIVER': app.config['DB_DRIVER']
    }
    try:
        cnn = pyodbc.connect(";".join(["%s=%s" % (key, config[key]) for key in config]))
        return cnn
    except pyodbc.Error as ex:
        return None


def get_cnn():
    return connect_db(current_app)


def release_cnn(cnn):
    cnn.close()
