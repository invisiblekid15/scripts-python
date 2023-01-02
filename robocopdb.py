import pymysql.cursors
import pymysql

if __name__ == "__main__":

    # Connect to the database
    connection = pymysql.connect(host='172.16.47.136',
                                 user='datalayer',
                                 password='Q@Usr@123',
                                 db='robocop',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `flightrobocoptasks`"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()
