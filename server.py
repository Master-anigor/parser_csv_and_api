#!flask/bin/python
import logging
from flask import Flask, request, jsonify

from db import Connection

app = Flask(__name__)
logging.basicConfig(level=logging.ERROR, filename="server.log", filemode="w")


def get_incedent(cursor, date_from=None, date_to=None, page=0, size=20):
    offset = size*page
    sql = "SELECT * FROM `police_department_calls` WHERE crime_id > 0"
    if date_from:
        sql += f" and `report_date` >= '{date_from}'"
    if date_to:
        sql += f" and `report_date` <='{date_to}'"
    sql += f" LIMIT {size} OFFSET {offset}"
    cursor.execute(sql)
    return cursor.fetchall()


@app.route('/', methods = ['GET'])
def index():
    data = []
    cnx, cursor = Connection.get_connection()
    if cnx and cursor:
        try:
            date_from = request.args.get('date_from', None)
            date_to = request.args.get('date_to', None)
            page = int(request.args.get('page', 0))
            size = int(request.args.get('size', 20))
            data = get_incedent(cursor, date_from, date_to, page, size)
        except Exception as e:
            logging.error(e)
        finally:
            if (cursor):
                cursor.close()
                cnx.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
