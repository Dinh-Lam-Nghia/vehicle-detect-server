from common import convert_to_dict
from db import *

def get_vehicle_staff():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"SELECT * FROM vehicle_staff WHERE active = 0"
    cursor.execute(sql)
    result = cursor.fetchall() 
    result = convert_to_dict(cursor, result)
    cursor.close()
    return result

def add_vehicle_staff(name: str, phone: str, model: str, plate_number: str, role: int, expires: str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO vehicle_staff (phone, vehicle_id, expires, role, name, vehicle_model) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (phone, plate_number, expires, role, name, model)
    cursor.execute(sql, val)
    conn.commit()

def remove_staff(id: str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"UPDATE vehicle_staff SET active = 1 WHERE id = '{id}'"
    cursor.execute(sql)
    conn.commit()

def update_staffs(id: str, name: str, phone: str, model: str, plate_number: str, role: int, expires: str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"UPDATE vehicle_staff SET phone = '{phone}', vehicle_id = '{plate_number}', expires = '{expires}', role = '{role}', name = '{name}', vehicle_model = '{model}' WHERE id = '{id}'"
    cursor.execute(sql)
    conn.commit()