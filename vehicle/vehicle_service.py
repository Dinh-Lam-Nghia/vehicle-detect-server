from common import convert_to_dict
from db import *

def get_vehicle_infor(email: str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"SELECT vehicle.*, user.phone FROM vehicle INNER JOIN user ON vehicle.user_id = user.id WHERE user.email = '{email}'"
    cursor.execute(sql)
    result = cursor.fetchall() 
    print(result)
    result = convert_to_dict(cursor, result)
    cursor.close()
    return result

def add_vehicle_infor(vehicle_id: int, role: int, vehicle_model: str, vehicle_color: str, vehicle_type: int, user_id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO vehicle (vehicle_id, role, vehicle_model, vehicle_color, vehicle_type, user_id) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (vehicle_id, role, vehicle_model, vehicle_color, vehicle_type, user_id)
    cursor.execute(sql, val)
    cursor.commit()

