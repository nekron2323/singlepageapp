import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL

load_dotenv()


USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DB_NAME = os.getenv('DB_NAME')
HOST = 'localhost'

app = Flask(__name__)
mysql = MySQL(app)

app.config.from_object(__name__)
app.config['MYSQL_HOST'] = HOST
app.config['MYSQL_USER'] = USER
app.config['MYSQL_PASSWORD'] = PASSWORD
app.config['MYSQL_DB'] = DB_NAME

CORS(app)

@app.route('/table', methods=['GET'])
def table():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM info")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=80)