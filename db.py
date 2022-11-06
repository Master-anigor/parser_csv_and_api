import mysql.connector


class Configuration:
    DB_HOST = '127.0.0.1'
    DB_PORT = '3306'
    DB_USER = 'root'
    DB_PASS = ''


class Connection:

    def __init__(self, ):
        cnx, cursor = self.get_connection()
        if not cursor:
            raise Exception('Database connection error')
        else:
            self.cnx = cnx
            self.cursor = cursor

    @staticmethod
    def get_connection():
        try:
            cnx = mysql.connector.connect(
                host=Configuration.DB_HOST,
                user=Configuration.DB_USER,
                password=Configuration.DB_PASS
            )
            cursor = cnx.cursor(buffered=True, dictionary=True)
            cursor.execute('USE police_department')
            return cnx, cursor

        except mysql.connector.Error as err:
            return False, False
