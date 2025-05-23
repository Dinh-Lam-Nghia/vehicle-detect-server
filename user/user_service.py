from common import convert_to_dict
from db import *

def check_user_exist(email: str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql_check_user = f"SELECT COUNT(*) FROM user WHERE email = '{email}'" 
    cursor.execute(sql_check_user)
    count = cursor.fetchone()[0]
    cursor.close()
    if count == 1:
        return True 
    else: 
        return False

def add_user(email: str, name: str, url_photo: str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO user (name, email, url_photo) VALUES (%s, %s, %s)"
    val = (name, email, url_photo)
    cursor.execute(sql, val)
    conn.commit()

def get_onlyOne_user(email: str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql_get_onlyOne_user = f"SELECT * FROM user WHERE email = '{email}'" 
    cursor.execute(sql_get_onlyOne_user)
    result = cursor.fetchall() 
    result = convert_to_dict(cursor, result)
    cursor.close()
    return result
