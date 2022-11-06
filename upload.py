# -*- coding: utf-8 -*-
import os
import logging
import time
from progress.bar import Bar

from db import Connection

path_file = 'police-department-calls-for-service.csv'
logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w")


def lenopenreadlines(filename):
    with open(filename) as f:
        return len(f.readlines())


def instert_row(cnx, cursor, row):
    data = row[:14]
    if len(row) > 14:
        data[13] = row[13] + row[14]
    sql = f"""
            INSERT INTO `police_department_calls`(`crime_id`, `crime_type`, `report_date`, `call_date`, `offense_date`, `call_time`, `call_date_time`, `disposition`, `address`, `city`, `state`, `agency_Id`, `address_type`, `common_location`) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
         """
    cursor.execute(sql, data)
    cnx.commit()


def main():
    start_time = time.time()
    cnx, cursor = Connection.get_connection()
    logging.info("Create Connection")
    if cnx and cursor:
        try:
            if os.path.exists(path_file):
                count_row = lenopenreadlines(path_file)
                bar = Bar('Processing', max=count_row)
                with open(path_file) as f:
                    row_first = False
                    for line in f:
                        bar.next()
                        logging.info(f"Load {bar.index}/{count_row} row")
                        if row_first:
                            data = line.split(',')
                            instert_row(cnx, cursor, data)
                        row_first = True
                bar.finish()
                print(f"Count row: {count_row}")
        except Exception as e:
            logging.error(e)
        finally:
            if (cursor):
                cursor.close()
                cnx.close()

    print("Time work: %s seconds" % (time.time() - start_time))
    logging.info("Finish program")

if __name__ == '__main__':
    main()
