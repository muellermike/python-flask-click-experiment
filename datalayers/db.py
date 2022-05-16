from distutils.command.config import config
from flask import current_app
import pymysql.cursors

def execute(sql, params, statement):
    """
    Runs an sql command on the database and returns result if there is one.
    """
    result = None

    conn = pymysql.connect(host = current_app.config["DB_URI"],
                            port = 3306,
                            user = current_app.config["DB_USER"],
                            password = current_app.config["DB_PW"],
                            db = current_app.config["DB_NAME"],
                            charset = "utf8mb4",
                            cursorclass = pymysql.cursors.DictCursor)

    try:
        with conn.cursor() as cursor:
            if statement == "SELECT":
                cursor.execute(sql, params)
                result = cursor.fetchall()
            elif statement == "INSERT MANY":
                cursor.executemany(sql, params)
                print(f"INSERT MANY done")
                conn.commit()
            else:
                cursor.execute(sql, params)
                result = conn.insert_id()
                print(f"result NOT SELECT: {result}")
                conn.commit()
    finally:
        conn.close()
    
    return result