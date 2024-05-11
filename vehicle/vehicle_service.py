from common import convert_to_dict
from db import *

def get_vehicle_infor(email: str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"SELECT vehicle.* FROM vehicle INNER JOIN user ON vehicle.user_id = user.id WHERE user.email = '{email}' AND active != 1"
    cursor.execute(sql)
    result = cursor.fetchall() 
    result = convert_to_dict(cursor, result)
    cursor.close()
    return result

def add_vehicle_infor(vehicle_id: str, role: int, vehicle_model: str, vehicle_color: str, vehicle_type: int, user_id: int, expires: str, phone: str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO vehicle (vehicle_id, role, vehicle_model, vehicle_color, vehicle_type, user_id, expires, phone, active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (vehicle_id, role, vehicle_model, vehicle_color, vehicle_type, user_id, expires, phone, 2)
    cursor.execute(sql, val)
    conn.commit()

def remove_active(vehicle_id: str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"UPDATE vehicle SET active = 1 WHERE vehicle_id = '{vehicle_id}'"
    cursor.execute(sql)
    conn.commit()

def update_vehicle_infor(vehicle_id: str, role: int, vehicle_color: str, expires: str, phone: str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"UPDATE vehicle SET role = '{role}', vehicle_color = '{vehicle_color}', expires = '{expires}', phone = '{phone}' WHERE vehicle_id = '{vehicle_id}'"
    cursor.execute(sql)
    conn.commit()

def get_all_vehicles():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"SELECT * FROM vehicle WHERE active <1" 
    cursor.execute(sql)
    result = cursor.fetchall() 
    result = convert_to_dict(cursor, result)
    cursor.close()
    return result 


