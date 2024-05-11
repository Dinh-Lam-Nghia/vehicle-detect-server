from common import convert_to_dict
from db import *

def get_logs():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"SELECT * FROM log"
    cursor.execute(sql)
    result = cursor.fetchall() 
    result = convert_to_dict(cursor, result)
    cursor.close()
    return result

def get_log_table(role: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = ""
    if (role == '0'):
        sql = f"SELECT vehicle.*, log.time, log.status, user.name FROM vehicle INNER JOIN user ON vehicle.user_id = user.id INNER JOIN log ON log.vehicle_id = vehicle.vehicle_id WHERE log.role = {role} AND  vehicle.active != 2;"
    else:
        # sql = f"SELECT vehicle_staff.*, log.time, log.status FROM log INNER JOIN vehicle_staff ON log.vehicle_id = vehicle_staff.id WHERE log.role = 1"
        sql = f"SELECT vehicle_staff.*, log.time, log.status FROM vehicle_staff INNER JOIN log ON vehicle_staff.vehicle_id = log.vehicle_id WHERE log.role = 1"
        
    cursor.execute(sql)
    result = cursor.fetchall() 
    result = convert_to_dict(cursor, result)
    cursor.close()
    return result

def get_all_vehicle_admin(role: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = ""
    if (role == '0'):
        # sql = f"SELECT vehicle.*, user.name FROM log INNER JOIN vehicle ON log.vehicle_id = vehicle.id INNER JOIN user ON vehicle.user_id = user.id WHERE log.role = '{role} AND vehicle.active != 2'"
                sql = f"SELECT vehicle.*, user.name FROM vehicle INNER JOIN user ON vehicle.user_id = user.id WHERE vehicle.active <1;"

    else:
        sql = f"SELECT vehicle_staff.* FROM vehicle_staff WHERE vehicle_staff.active <1"
        # sql = f"SELECT vehicle.*, vehicle_staff.name FROM vehicle INNER JOIN vehicle_staff ON vehicle.user_id = vehicle_staff.id WHERE vehicle.active < 1;"
    cursor.execute(sql)
    result = cursor.fetchall() 
    result = convert_to_dict(cursor, result)
    cursor.close()
    return result

def get_request():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"SELECT vehicle.*, user.name FROM vehicle INNER JOIN user ON user.id = vehicle.user_id WHERE active = 2"
    cursor.execute(sql)
    result = cursor.fetchall() 
    result = convert_to_dict(cursor, result)
    cursor.close()
    return result 

def accpect_request(vehicle_id : str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"UPDATE vehicle SET active = 0 WHERE id = '{vehicle_id}'"
    cursor.execute(sql)
    conn.commit()

def remove_request(id : str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"UPDATE vehicle SET active = 1 WHERE id = '{id}'"
    cursor.execute(sql)
    conn.commit()