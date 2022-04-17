import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL

load_dotenv()


app = Flask(__name__)
mysql = MySQL(app)

app.config.from_object(__name__)
app.config['MYSQL_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_DB'] = os.getenv('DB_NAME')
app.config['MYSQL_USER'] = os.getenv('USER')
app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORD')

CORS(app)

@app.route('/table', methods=['GET'])
def table():
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM {os.getenv('TABLE_NAME')}")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=80)