from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def favorite_colors():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'colorsdb'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name+'_working': color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index():
    return json.dumps({'favorite_colors': favorite_colors()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')